from flask import Flask, request, jsonify, render_template
import PyPDF2
import re
import random
from collections import defaultdict
import nltk
import string
import os
import tempfile

# Download required NLTK data automatically
def download_nltk_resources():
    resources = {
        'punkt': 'tokenizers/punkt',
        'stopwords': 'corpora/stopwords',
        'punkt_tab': 'tokenizers/punkt_tab'
    }
    
    for resource, path in resources.items():
        try:
            nltk.data.find(path)
            print(f"✓ {resource} already available")
        except LookupError:
            print(f"📥 Downloading {resource}...")
            try:
                nltk.download(resource, quiet=True)
                print(f"✓ {resource} downloaded successfully")
            except Exception as e:
                print(f"⚠ Could not download {resource}: {e}")

# Download resources when the app starts
print("Initializing NLTK resources...")
download_nltk_resources()

# Now import the NLTK components after ensuring they're available
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

app = Flask(__name__)

class PDFQuestionGenerator:
    def __init__(self):
        try:
            self.stop_words = set(stopwords.words('english'))
        except:
            # Fallback stopwords if NLTK stopwords aren't available
            self.stop_words = {
                'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 
                'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 
                'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 
                "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 
                'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 
                'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 
                'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 
                'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 
                'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 
                'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 
                'through', 'during', 'before', 'after', 'above', 'below', 'to', 
                'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 
                'again', 'further', 'then', 'once', 'here', 'there', 'when', 
                'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 
                'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 
                'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 
                'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 
                'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', 
                "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 
                'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', 
                "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 
                'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', 
                "won't", 'wouldn', "wouldn't"
            }
        
    def extract_text_from_pdf(self, pdf_file):
        """Extract text from PDF file object"""
        text = ""
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return ""
    
    def preprocess_text(self, text):
        """Clean and preprocess the extracted text"""
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s\.\,\?\!]', '', text)
        return text.strip()
    
    def simple_sentence_split(self, text):
        """Simple sentence splitting that doesn't rely on NLTK punkt"""
        # Split on sentence endings
        sentences = re.split(r'[.!?]+', text)
        # Clean up sentences
        sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
        return sentences
    
    def simple_word_tokenize(self, text):
        """Simple word tokenization that doesn't rely on NLTK"""
        # Remove punctuation and split on whitespace
        text = re.sub(r'[^\w\s]', ' ', text)
        words = text.lower().split()
        return words
    
    def extract_key_phrases(self, text, num_phrases=20):
        """Extract important phrases and key terms from text"""
        try:
            # Try using NLTK first
            sentences = sent_tokenize(text)
        except:
            # Fallback to simple sentence splitting
            sentences = self.simple_sentence_split(text)
        
        key_phrases = []
        
        for sentence in sentences:
            try:
                # Try using NLTK tokenization
                words = word_tokenize(sentence.lower())
            except:
                # Fallback to simple tokenization
                words = self.simple_word_tokenize(sentence)
            
            # Filter words
            words = [word for word in words if word not in self.stop_words and word not in string.punctuation]
            words = [word for word in words if len(word) > 2 and word.isalpha()]
            
            # Extract 2-word phrases
            for i in range(len(words) - 1):
                phrase = f"{words[i]} {words[i+1]}"
                if len(phrase.split()) == 2:
                    key_phrases.append(phrase)
            
            key_phrases.extend(words)
        
        phrase_freq = defaultdict(int)
        for phrase in key_phrases:
            phrase_freq[phrase] += 1
        
        common_phrases_to_avoid = {'said that', 'one of', 'part of', 'type of', 'kind of'}
        sorted_phrases = sorted(phrase_freq.items(), key=lambda x: x[1], reverse=True)
        top_phrases = [phrase for phrase, freq in sorted_phrases 
                      if phrase not in common_phrases_to_avoid and freq > 1][:num_phrases]
        
        return top_phrases
    
    def find_sentences_with_phrases(self, text, phrases):
        """Find sentences that contain the key phrases"""
        try:
            sentences = sent_tokenize(text)
        except:
            sentences = self.simple_sentence_split(text)
            
        phrase_sentences = {}
        
        for phrase in phrases:
            for sentence in sentences:
                if phrase.lower() in sentence.lower():
                    phrase_sentences[phrase] = sentence
                    break
        
        return phrase_sentences
    
    def generate_multiple_choice_questions(self, phrase_sentences, num_questions=10):
        """Generate multiple choice questions based on key phrases"""
        questions = []
        phrases = list(phrase_sentences.keys())
        
        if len(phrases) < 4:
            return questions
        
        for _ in range(min(num_questions, len(phrases))):
            if len(phrases) < 4:
                break
                
            target_phrase = random.choice(phrases)
            original_sentence = phrase_sentences[target_phrase]
            phrases.remove(target_phrase)
            
            question_text = original_sentence.replace(target_phrase, "__________")
            
            distractors = random.sample([p for p in phrases if p != target_phrase], 3)
            
            options = [target_phrase] + distractors
            random.shuffle(options)
            
            correct_index = options.index(target_phrase)
            
            questions.append({
                'question': f"Complete the sentence: {question_text}",
                'options': options,
                'correct_answer': correct_index,
                'target_phrase': target_phrase
            })
        
        return questions
    
    def generate_definition_questions(self, text, num_questions=5):
        """Generate definition-based questions"""
        try:
            sentences = sent_tokenize(text)
        except:
            sentences = self.simple_sentence_split(text)
            
        questions = []
        
        definition_patterns = [
            r'is (?:a|an|the) [^\.]+',
            r'refers to [^\.]+',
            r'means [^\.]+',
            r'defined as [^\.]+'
        ]
        
        definition_sentences = []
        for sentence in sentences:
            for pattern in definition_patterns:
                if re.search(pattern, sentence.lower()):
                    words = self.simple_word_tokenize(sentence)
                    if len(words) > 3:
                        term = ' '.join(words[:3])
                        definition_sentences.append((term, sentence))
                    break
        
        for term, sentence in definition_sentences[:num_questions]:
            fake_definitions = [
                "A completely different concept",
                "An unrelated technical term",
                "A misleading description",
                "An opposite meaning"
            ]
            
            actual_definition = " ".join(sentence.split()[3:])[:100] + "..."
            
            options = [actual_definition] + random.sample(fake_definitions, 3)
            random.shuffle(options)
            correct_index = options.index(actual_definition)
            
            questions.append({
                'question': f"What is the definition of '{term}'?",
                'options': options,
                'correct_answer': correct_index,
                'type': 'definition'
            })
        
        return questions
    
    def generate_fill_blank_questions(self, text, num_questions=5):
        """Generate simple fill-in-the-blank questions as fallback"""
        try:
            sentences = sent_tokenize(text)
        except:
            sentences = self.simple_sentence_split(text)
            
        questions = []
        
        for sentence in sentences:
            if len(sentence) > 50:  # Use substantial sentences
                words = sentence.split()
                if len(words) > 8:
                    # Remove a key word (usually in the middle)
                    key_word_index = random.randint(3, len(words) - 3)
                    key_word = words[key_word_index]
                    
                    # Create question
                    question_sentence = ' '.join(words[:key_word_index] + ['__________'] + words[key_word_index+1:])
                    
                    # Generate options
                    correct_answer = key_word
                    options = [correct_answer]
                    
                    # Add similar looking but wrong options
                    similar_words = [
                        words[key_word_index - 1] if key_word_index > 0 else "previous",
                        words[key_word_index + 1] if key_word_index < len(words) - 1 else "next",
                        "different", "alternative", "various"
                    ]
                    
                    options.extend(random.sample([w for w in similar_words if w != correct_answer], 3))
                    random.shuffle(options)
                    correct_index = options.index(correct_answer)
                    
                    questions.append({
                        'question': question_sentence,
                        'options': options,
                        'correct_answer': correct_index
                    })
                    
                    if len(questions) >= num_questions:
                        break
        
        return questions
    
    def process_pdf_text(self, text, num_questions=15):
        """Process text and generate questions"""
        if not text:
            return []
        
        clean_text = self.preprocess_text(text)
        
        # Try to generate questions using the main method
        key_phrases = self.extract_key_phrases(clean_text)
        phrase_sentences = self.find_sentences_with_phrases(clean_text, key_phrases)
        
        mc_questions = self.generate_multiple_choice_questions(phrase_sentences, num_questions//2)
        def_questions = self.generate_definition_questions(clean_text, num_questions//3)
        
        all_questions = mc_questions + def_questions
        
        # If we don't have enough questions, use fallback method
        if len(all_questions) < num_questions:
            fill_questions = self.generate_fill_blank_questions(clean_text, num_questions - len(all_questions))
            all_questions.extend(fill_questions)
        
        random.shuffle(all_questions)
        
        return all_questions[:num_questions]

# Initialize the question generator
generator = PDFQuestionGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    try:
        if 'pdf' not in request.files:
            return jsonify({'error': 'No PDF file provided'}), 400
        
        pdf_file = request.files['pdf']
        if pdf_file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not pdf_file.filename.lower().endswith('.pdf'):
            return jsonify({'error': 'File must be a PDF'}), 400
        
        # Extract text from PDF
        text = generator.extract_text_from_pdf(pdf_file)
        
        if not text:
            return jsonify({'error': 'Could not extract text from PDF. The PDF might be scanned or encrypted.'}), 400
        
        # Generate questions
        num_questions = int(request.form.get('num_questions', 10))
        questions = generator.process_pdf_text(text, num_questions)
        
        if not questions:
            return jsonify({'error': 'Could not generate questions from the PDF content. Try a different PDF with more text content.'}), 400
        
        return jsonify({
            'success': True,
            'questions': questions,
            'total_questions': len(questions)
        })
        
    except Exception as e:
        return jsonify({'error': f'Processing error: {str(e)}'}), 500

if __name__ == '__main__':
    print("🚀 Starting PDF Question Generator...")
    print("📖 Access the application at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)