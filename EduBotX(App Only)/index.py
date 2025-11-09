from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
import PyPDF2
import google.generativeai as genai
import json
import os
import secrets
import time
import logging
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}
app.config['SECRET_KEY'] = 'KIO'  # Change this to a random secret key

CORS(app)

# Configuration - FREE Google Gemini API
GEMINI_API_KEY = "AIzaSyD91QFU7xr_IOt02AJWvVGXMqRmRdcn1Cc"

# Simple user storage (in production, use a database)
users = {
    'admin': generate_password_hash('admin123')  # Default admin user
}

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RateLimiter:
    def __init__(self, max_requests=15, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []
    
    def wait_if_needed(self):
        now = time.time()
        # Remove requests outside the current time window
        self.requests = [req_time for req_time in self.requests 
                        if now - req_time < self.time_window]
        
        if len(self.requests) >= self.max_requests:
            oldest_request = min(self.requests)
            sleep_time = oldest_request + self.time_window - now
            if sleep_time > 0:
                logger.info(f"Rate limit reached. Waiting {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)
            # Remove the oldest request after waiting
            self.requests = self.requests[1:]
        
        self.requests.append(now)

class PDFQuestionGenerator:
    def __init__(self, gemini_api_key):
        self.gemini_api_key = gemini_api_key
        genai.configure(api_key=gemini_api_key)
        self.model = genai.GenerativeModel('learnlm-2.0-flash-experimental')
        self.rate_limiter = RateLimiter(max_requests=10, time_window=60)  # 10 requests per minute
        self.last_request_time = 0
        self.min_request_interval = 2  # Minimum 2 seconds between requests
    
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
            logger.error(f"Error reading PDF: {e}")
            return None
    
    def _enforce_rate_limit(self):
        """Enforce rate limiting between requests"""
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        
        if time_since_last_request < self.min_request_interval:
            sleep_time = self.min_request_interval - time_since_last_request
            time.sleep(sleep_time)
        
        self.rate_limiter.wait_if_needed()
        self.last_request_time = time.time()
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=60),
        retry=retry_if_exception(lambda e: "429" in str(e) or "500" in str(e) or "503" in str(e))
    )
    def _make_api_call(self, prompt):
        """Make API call with retry logic"""
        self._enforce_rate_limit()
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            error_str = str(e)
            if "429" in error_str:
                logger.warning("Rate limit hit, will retry with exponential backoff")
            elif "500" in error_str or "503" in error_str:
                logger.warning("Server error, will retry")
            else:
                logger.error(f"API error: {e}")
            raise e
    
    def generate_questions(self, text, question_type="multiple_choice", num_questions=5):
        """Generate questions from text using Google Gemini or fallback"""
        # If text is too long, truncate it
        if len(text) > 4000:
            text = text[:4000]
            logger.info("Text truncated to 4000 characters for API call")
            
        try:
            if question_type == "multiple_choice":
                prompt = self._create_multiple_choice_prompt(text, num_questions)
            elif question_type == "true_false":
                prompt = self._create_true_false_prompt(text, num_questions)
            elif question_type == "identification":
                prompt = self._create_identification_prompt(text, num_questions)
            else:
                prompt = self._create_multiple_choice_prompt(text, num_questions)
            
            logger.info(f"Making API call for {num_questions} {question_type} questions")
            questions_json = self._make_api_call(prompt)
            
            # Clean the response
            questions_json = self._clean_json_response(questions_json)
            
            # Parse JSON
            questions_data = json.loads(questions_json)
            logger.info(f"Successfully generated {len(questions_data.get('questions', []))} questions")
            return questions_data
            
        except Exception as e:
            logger.error(f"Gemini API error after retries: {e}")
            logger.info("Falling back to local question generation")
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

        Text content: {text}

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

        Text content: {text}

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

        Text content: {text}

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
        
        logger.info(f"Generated {len(questions['questions'])} fallback questions")
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

def login_required(f):
    """Decorator to require login for specific routes"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return jsonify({'success': False, 'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'success': False, 'error': 'Username and password required'})
    
    if username in users and check_password_hash(users[username], password):
        session['logged_in'] = True
        session['username'] = username
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'error': 'Invalid credentials'})

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True, 'message': 'Logout successful'})

@app.route('/check-auth')
def check_auth():
    if session.get('logged_in'):
        return jsonify({'authenticated': True, 'username': session.get('username')})
    return jsonify({'authenticated': False})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'success': False, 'error': 'Username and password required'})
    
    if username in users:
        return jsonify({'success': False, 'error': 'Username already exists'})
    
    users[username] = generate_password_hash(password)
    return jsonify({'success': True, 'message': 'Registration successful'})

@app.route('/upload', methods=['POST'])
@login_required
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
            
            logger.info(f"Processing PDF for user {session.get('username')}: {filename}")
            
            # Get question type from request
            question_type = request.form.get('question_type', 'multiple_choice')
            num_questions = int(request.form.get('num_questions', 5))
            
            # Limit number of questions to avoid excessive API calls
            num_questions = min(num_questions, 10)  # Max 10 questions per request
            
            # Extract text from PDF
            text = generator.extract_text_from_pdf(filepath)
            
            if not text:
                os.remove(filepath)
                return jsonify({'success': False, 'error': 'Could not extract text from PDF. The PDF might be scanned or image-based.'})
            
            logger.info(f"Extracted {len(text)} characters")
            logger.info(f"Generating {num_questions} {question_type} questions")
            
            # Generate questions
            questions = generator.generate_questions(text, question_type, num_questions)
            
            if not questions:
                os.remove(filepath)
                return jsonify({'success': False, 'error': 'Failed to generate questions. Please try again.'})
            
            logger.info(f"Generated {len(questions['questions'])} questions")
            
            # Save questions to user-specific file
            questions_file = f'generated_questions_{session.get("username")}.json'
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
            logger.error(f"Error in upload: {e}")
            if 'filepath' in locals() and os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'success': False, 'error': str(e)})
    
    return jsonify({'success': False, 'error': 'Invalid file type. Please upload a PDF file.'})

@app.route('/questions')
@login_required
def get_questions():
    try:
        questions_file = f'generated_questions_{session.get("username")}.json'
        with open(questions_file, 'r') as f:
            questions = json.load(f)
        return jsonify(questions)
    except:
        return jsonify({'error': 'No questions generated yet'})

@app.route('/test-gemini')
@login_required
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
    print("🔐 Login system enabled")
    print("👤 Default credentials: admin / admin123")
    print("📚 Pure software version - No ESP32 integration")
    print("🌐 Open http://localhost:5000 in your browser")
    print("⚡ Rate limiting enabled: 10 requests per minute")
    app.run(host='0.0.0.0', port=5000, debug=True)