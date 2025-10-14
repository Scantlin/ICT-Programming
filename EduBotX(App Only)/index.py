from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import PyPDF2
import google.generativeai as genai
import json
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# Configuration - FREE Google Gemini API
GEMINI_API_KEY = "AIzaSyD91QFU7xr_IOt02AJWvVGXMqRmRdcn1Cc"  # Get free key from: https://makersuite.google.com/app/apikey

class PDFQuestionGenerator:
    def __init__(self, gemini_api_key):
        genai.configure(api_key=gemini_api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash-lite')
        print("✅ Gemini API configured successfully")

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
    
    def generate_questions(self, text, question_type="multiple_choice", num_questions=5):
        """Generate questions from text using Google Gemini or fallback"""
        # If no API key or model, use fallback immediately
        if not self.model:
            return self.fallback_question_generation(text, question_type, num_questions)
            
        try:
            if question_type == "multiple_choice":
                prompt = self._create_multiple_choice_prompt(text, num_questions)
            elif question_type == "true_false":
                prompt = self._create_true_false_prompt(text, num_questions)
            elif question_type == "identification":
                prompt = self._create_identification_prompt(text, num_questions)
            else:
                prompt = self._create_multiple_choice_prompt(text, num_questions)
            
            response = self.model.generate_content(prompt)
            questions_json = response.text.strip()
            
            # Clean the response
            questions_json = self._clean_json_response(questions_json)
            
            # Parse JSON
            questions_data = json.loads(questions_json)
            return questions_data
            
        except Exception as e:
            print(f"Gemini API error: {e}")
            return self.fallback_question_generation(text, question_type, num_questions)
    
    def _create_multiple_choice_prompt(self, text, num_questions):
        return f"""
        Create {num_questions} educational multiple-choice questions from the following text.
        Format the response as valid JSON only with this exact structure:

        {{
            "questions": [
                {{
                    "question": "question text here",
                    "options": ["Option A text", "Option B text", "Option C text", "Option D text"],
                    "correct_answer": "A",
                    "type": "multiple_choice"
                }}
            ]
        }}

        Text content: {text[:3000]}

        Important: Return ONLY the JSON, no other text, no markdown, no explanations.
        Make sure the questions are educational and relevant to the text.
        """
    
    def _create_true_false_prompt(self, text, num_questions):
        return f"""
        Create {num_questions} True or False questions from the following text.
        Format the response as valid JSON only with this exact structure:

        {{
            "questions": [
                {{
                    "question": "statement here that can be true or false",
                    "correct_answer": "True",
                    "type": "true_false"
                }}
            ]
        }}

        Text content: {text[:3000]}

        Important: Return ONLY the JSON, no other text. Make statements that are clearly true or false based on the text.
        """
    
    def _create_identification_prompt(self, text, num_questions):
        return f"""
        Create {num_questions} identification questions from the following text.
        Format the response as valid JSON only with this exact structure:

        {{
            "questions": [
                {{
                    "question": "question asking to identify something",
                    "correct_answer": "the correct identification answer",
                    "type": "identification"
                }}
            ]
        }}

        Text content: {text[:3000]}

        Important: Return ONLY the JSON, no other text. Create questions that ask to identify specific concepts, terms, or facts.
        """
    
    def _clean_json_response(self, response_text):
        """Clean the API response to extract valid JSON"""
        # Remove markdown code blocks
        if response_text.startswith('```json'):
            response_text = response_text[7:].strip()
        if response_text.endswith('```'):
            response_text = response_text[:-3].strip()
        if response_text.startswith('```'):
            response_text = response_text[3:].strip()
        return response_text
    
    def fallback_question_generation(self, text, question_type, num_questions):
        """Fallback method if API fails or no API key"""
        import re
        
        # Split text into sentences
        sentences = re.split(r'[.!?]+', text)
        questions = {"questions": []}
        
        count = 0
        for sentence in sentences:
            if len(sentence.strip()) > 30 and count < num_questions:
                words = sentence.strip().split()
                if len(words) > 5:
                    key_phrase = ' '.join(words[2:5])
                    
                    if question_type == "multiple_choice":
                        question = self._create_fallback_multiple_choice(key_phrase, count)
                    elif question_type == "true_false":
                        question = self._create_fallback_true_false(key_phrase, count)
                    elif question_type == "identification":
                        question = self._create_fallback_identification(key_phrase, count)
                    else:
                        question = self._create_fallback_multiple_choice(key_phrase, count)
                    
                    questions["questions"].append(question)
                    count += 1
        
        # Fill remaining questions if needed
        while len(questions["questions"]) < num_questions:
            if question_type == "multiple_choice":
                question = self._create_fallback_multiple_choice("the content", len(questions["questions"]))
            elif question_type == "true_false":
                question = self._create_fallback_true_false("the content", len(questions["questions"]))
            elif question_type == "identification":
                question = self._create_fallback_identification("the content", len(questions["questions"]))
            else:
                question = self._create_fallback_multiple_choice("the content", len(questions["questions"]))
            
            questions["questions"].append(question)
        
        return questions
    
    def _create_fallback_multiple_choice(self, key_phrase, index):
        templates = [
            f"What is the main idea discussed about '{key_phrase}'?",
            f"Based on the text, what can be inferred about '{key_phrase}'?",
            f"What is the primary focus regarding '{key_phrase}'?",
            f"What key point is made about '{key_phrase}'?"
        ]
        
        return {
            "question": templates[index % len(templates)],
            "options": [
                "It explains fundamental concepts and principles",
                "It provides specific examples and case studies", 
                "It describes processes and methodologies",
                "It presents arguments and perspectives"
            ],
            "correct_answer": "A",
            "type": "multiple_choice"
        }
    
    def _create_fallback_true_false(self, key_phrase, index):
        templates = [
            f"The text provides detailed information about {key_phrase}.",
            f"{key_phrase} is considered an important concept in the text.",
            f"The author emphasizes the significance of {key_phrase}.",
            f"{key_phrase} is described as a complex topic in the text."
        ]
        
        return {
            "question": templates[index % len(templates)],
            "correct_answer": "True",
            "type": "true_false"
        }
    
    def _create_fallback_identification(self, key_phrase, index):
        templates = [
            f"What term describes {key_phrase} in the text?",
            f"Identify the main concept related to {key_phrase}.",
            f"What is the key methodology mentioned for {key_phrase}?",
            f"Name the primary element associated with {key_phrase}."
        ]
        
        answers = [
            "Fundamental principle",
            "Core concept",
            "Primary methodology",
            "Key element"
        ]
        
        return {
            "question": templates[index % len(templates)],
            "correct_answer": answers[index % len(answers)],
            "type": "identification"
        }

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
            
            # Get question type from request
            question_type = request.form.get('question_type', 'multiple_choice')
            num_questions = int(request.form.get('num_questions', 5))
            
            # Extract text from PDF
            text = generator.extract_text_from_pdf(filepath)
            
            if not text:
                os.remove(filepath)
                return jsonify({'success': False, 'error': 'Could not extract text from PDF. The PDF might be scanned or image-based.'})
            
            print(f"Extracted {len(text)} characters")
            print(f"Generating {num_questions} {question_type} questions")
            
            # Generate questions
            questions = generator.generate_questions(text, question_type, num_questions)
            
            if not questions:
                os.remove(filepath)
                return jsonify({'success': False, 'error': 'Failed to generate questions. Please try again.'})
            
            print(f"Generated {len(questions['questions'])} questions")
            
            # Save questions to file
            questions_file = 'generated_questions.json'
            with open(questions_file, 'w') as f:
                json.dump(questions, f, indent=2)
            
            # Clean up uploaded file
            os.remove(filepath)
            
            return jsonify({
                'success': True,
                'message': f'Successfully generated {len(questions["questions"])} {question_type.replace("_", " ")} questions',
                'questions': questions,
                'questions_count': len(questions['questions']),
                'question_type': question_type
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

@app.route('/test-gemini')
def test_gemini():
    """Test endpoint to check if Gemini API is working"""
    try:
        if not generator.model:
            return jsonify({
                'success': False,
                'error': 'Gemini API not configured. Using fallback mode.',
                'using_fallback': True
            })
            
        test_text = "The water cycle describes how water evaporates from the Earth's surface, rises into the atmosphere, cools and condenses into rain or snow in clouds, and falls again to the surface as precipitation."
        questions = generator.generate_questions(test_text, "multiple_choice", 2)
        
        return jsonify({
            'success': True,
            'message': 'Gemini API is working!',
            'test_questions': questions,
            'using_fallback': False
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Gemini API test failed: {str(e)}',
            'using_fallback': True
        })

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    print("🎓 Starting Educational Assistant Server...")
    print("📚 Pure software version - No ESP32 integration")
    print("🔑 API Status:", "Configured" if generator.model else "Using Fallback (No API Key)")
    print("🌐 Open http://localhost:5000 in your browser")
    app.run(host='0.0.0.0', port=5000, debug=True)