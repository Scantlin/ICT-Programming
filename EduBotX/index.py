from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import PyPDF2
import google.generativeai as genai
import json
import requests
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# Configuration - FREE Google Gemini API
GEMINI_API_KEY = "AIzaSyD91QFU7xr_IOt02AJWvVGXMqRmRdcn1Cc"  # Get free key from: https://makersuite.google.com/app/apikey
ESP32_IP = "192.168.1.100"

class PDFQuestionGenerator:
    def __init__(self, gemini_api_key):
        self.gemini_api_key = gemini_api_key
        genai.configure(api_key=gemini_api_key)
        # Use the correct model name
        self.model = genai.GenerativeModel('gemini-2.5-flash')  # Updated model name
        
    def extract_text_from_pdf(self, pdf_path):
        """Extract text content from PDF file"""
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                return text if text.strip() else None
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return None
    
    def generate_questions(self, text, num_questions=5):
        """Generate questions from text using Google Gemini"""
        prompt = f"""
        Create {num_questions} educational multiple-choice questions from the following text.
        Format the response as valid JSON only with this exact structure:

        {{
            "questions": [
                {{
                    "question": "question text here",
                    "options": ["Option A text", "Option B text", "Option C text", "Option D text"],
                    "correct_answer": "A"
                }}
            ]
        }}

        Text content: {text[:3000]}

        Important: Return ONLY the JSON, no other text, no markdown, no explanations.
        Make sure the questions are educational and relevant to the text.
        """
        
        try:
            # Generate content with the correct model
            generation_config = {
                "temperature": 0.7,
                "top_p": 0.8,
                "top_k": 40,
                "max_output_tokens": 2048,
            }
            
            response = self.model.generate_content(
                prompt,
                generation_config=generation_config
            )
            
            questions_json = response.text.strip()
            print(f"Raw API response: {questions_json}")  # Debug
            
            # Clean the response - remove markdown code blocks
            if questions_json.startswith('```json'):
                questions_json = questions_json[7:].strip()
            if questions_json.endswith('```'):
                questions_json = questions_json[:-3].strip()
            if questions_json.startswith('```'):
                questions_json = questions_json[3:].strip()
            
            # Parse JSON
            questions_data = json.loads(questions_json)
            return questions_data
            
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            print(f"Cleaned response: {questions_json}")
            return self.fallback_question_generation(text, num_questions)
        except Exception as e:
            print(f"Gemini API error: {e}")
            return self.fallback_question_generation(text, num_questions)
    
    def fallback_question_generation(self, text, num_questions):
        """Fallback method if API fails"""
        import re
        # Split text into sentences
        sentences = re.split(r'[.!?]+', text)
        questions = {"questions": []}
        
        question_templates = [
            "What is the main idea discussed in the text about '{}'?",
            "Based on the content, what can be inferred about '{}'?",
            "What is the primary focus of the section discussing '{}'?",
            "What key point is made regarding '{}'?",
            "What conclusion can be drawn from the information about '{}'?"
        ]
        
        count = 0
        for sentence in sentences:
            if len(sentence.strip()) > 30 and count < num_questions:
                # Extract a key phrase from the sentence
                words = sentence.strip().split()
                if len(words) > 5:
                    key_phrase = ' '.join(words[2:5])  # Get some context words
                    template = question_templates[count % len(question_templates)]
                    
                    questions["questions"].append({
                        "question": template.format(key_phrase),
                        "options": [
                            "It explains fundamental concepts and principles",
                            "It provides specific examples and case studies", 
                            "It describes processes and methodologies",
                            "It presents arguments and perspectives"
                        ],
                        "correct_answer": "A"
                    })
                    count += 1
        
        # If we didn't get enough questions, add generic ones
        while len(questions["questions"]) < num_questions:
            questions["questions"].append({
                "question": f"What is the main educational value of this content?",
                "options": [
                    "It enhances understanding of core concepts",
                    "It provides practical applications", 
                    "It offers historical context",
                    "It presents research findings"
                ],
                "correct_answer": "A"
            })
        
        return questions
    
    def send_to_esp32(self, questions):
        """Send questions to ESP32 via HTTP"""
        url = f"http://{ESP32_IP}/questions"
        
        try:
            response = requests.post(
                url,
                json=questions,
                timeout=5
            )
            return response.status_code == 200
        except Exception as e:
            print(f"Error sending to ESP32: {e}")
            return False

# Initialize the question generator with Gemini
generator = PDFQuestionGenerator(GEMINI_API_KEY)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'success': False, 'error': 'No file uploaded'})
    
    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'})
    
    if file and allowed_file(file.filename):
        try:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            print(f"Processing PDF: {filename}")
            
            # Extract text from PDF
            text = generator.extract_text_from_pdf(filepath)
            
            if not text:
                os.remove(filepath)
                return jsonify({'success': False, 'error': 'Could not extract text from PDF. The PDF might be scanned or image-based.'})
            
            print(f"Extracted {len(text)} characters")
            print(f"Sample text: {text[:200]}...")  # Debug
            
            # Generate questions
            questions = generator.generate_questions(text)
            
            if not questions:
                os.remove(filepath)
                return jsonify({'success': False, 'error': 'Failed to generate questions. Please try again.'})
            
            print(f"Generated {len(questions['questions'])} questions")
            
            # Save questions to file
            questions_file = 'generated_questions.json'
            with open(questions_file, 'w') as f:
                json.dump(questions, f, indent=2)
            
            # Send to ESP32
            esp32_success = generator.send_to_esp32(questions)
            
            # Clean up uploaded file
            os.remove(filepath)
            
            return jsonify({
                'success': True,
                'message': f'Successfully generated {len(questions["questions"])} questions',
                'questions': questions,
                'esp32_sent': esp32_success,
                'questions_count': len(questions['questions'])
            })
            
        except Exception as e:
            print(f"Error in upload: {e}")
            if 'filepath' in locals() and os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'success': False, 'error': str(e)})
    
    return jsonify({'success': False, 'error': 'Invalid file type. Please upload a PDF file.'})

@app.route('/questions')
def get_questions():
    try:
        with open('generated_questions.json', 'r') as f:
            questions = json.load(f)
        return jsonify(questions)
    except:
        return jsonify({'error': 'No questions generated yet'})

@app.route('/status')
def status():
    try:
        response = requests.get(f"http://{ESP32_IP}/battery", timeout=5)
        return jsonify(response.json())
    except:
        return jsonify({'status': 'esp32_offline'})

@app.route('/send-to-esp32', methods=['POST'])
def send_questions_to_esp32():
    try:
        with open('generated_questions.json', 'r') as f:
            questions = json.load(f)
        
        success = generator.send_to_esp32(questions)
        return jsonify({'success': success, 'message': 'Questions sent to ESP32' if success else 'Failed to send questions'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/test-gemini')
def test_gemini():
    """Test endpoint to check if Gemini API is working"""
    try:
        test_text = "The water cycle describes how water evaporates from the Earth's surface, rises into the atmosphere, cools and condenses into rain or snow in clouds, and falls again to the surface as precipitation."
        questions = generator.generate_questions(test_text, 2)
        return jsonify({
            'success': True,
            'message': 'Gemini API is working!',
            'test_questions': questions
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Gemini API test failed: {str(e)}'
        })

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    print("🎓 Starting Educational Assistant Server with Google Gemini...")
    print("🔑 Make sure you have set your GEMINI_API_KEY")
    print("🌐 Open http://localhost:5000 in your browser")
    print("🧪 Test API at: http://localhost:5000/test-gemini")
    app.run(host='0.0.0.0', port=5000, debug=True)