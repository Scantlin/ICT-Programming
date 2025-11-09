import PyPDF2
import re
import random
from collections import defaultdict
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class PDFQuestionGenerator:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        
    def extract_text_from_pdf(self, pdf_path):
        """Extract text from PDF file"""
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            return text
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return ""
    
    def preprocess_text(self, text):
        """Clean and preprocess the extracted text"""
        # Remove extra whitespace and newlines
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters but keep sentence structure
        text = re.sub(r'[^\w\s\.\,\?\!]', '', text)
        return text.strip()
    
    def extract_key_phrases(self, text, num_phrases=20):
        """Extract important phrases and key terms from text"""
        sentences = sent_tokenize(text)
        key_phrases = []
        
        for sentence in sentences:
            # Tokenize and clean words
            words = word_tokenize(sentence.lower())
            words = [word for word in words if word not in self.stop_words and word not in string.punctuation]
            words = [word for word in words if len(word) > 2]  # Remove very short words
            
            # Extract noun phrases (simple pattern-based)
            for i in range(len(words) - 1):
                # Look for adjective-noun or noun-noun patterns
                phrase = f"{words[i]} {words[i+1]}"
                if len(phrase.split()) == 2:
                    key_phrases.append(phrase)
            
            # Add important single words
            key_phrases.extend([word for word in words if word.isalpha()])
        
        # Get most frequent phrases
        phrase_freq = defaultdict(int)
        for phrase in key_phrases:
            phrase_freq[phrase] += 1
        
        # Return top phrases, avoiding very common ones
        common_phrases_to_avoid = {'said that', 'one of', 'part of', 'type of', 'kind of'}
        sorted_phrases = sorted(phrase_freq.items(), key=lambda x: x[1], reverse=True)
        top_phrases = [phrase for phrase, freq in sorted_phrases 
                      if phrase not in common_phrases_to_avoid and freq > 1][:num_phrases]
        
        return top_phrases
    
    def find_sentences_with_phrases(self, text, phrases):
        """Find sentences that contain the key phrases"""
        sentences = sent_tokenize(text)
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
            print("Not enough key phrases found to generate quality questions.")
            return questions
        
        for _ in range(min(num_questions, len(phrases))):
            if len(phrases) < 4:
                break
                
            # Select a target phrase and its sentence
            target_phrase = random.choice(phrases)
            original_sentence = phrase_sentences[target_phrase]
            phrases.remove(target_phrase)
            
            # Create question by blanking out the target phrase
            question_text = original_sentence.replace(target_phrase, "__________")
            
            # Generate distractors (wrong answers)
            distractors = random.sample([p for p in phrases if p != target_phrase], 3)
            
            # Combine options
            options = [target_phrase] + distractors
            random.shuffle(options)
            
            # Find correct answer index
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
        sentences = sent_tokenize(text)
        questions = []
        
        # Look for definition patterns
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
                    # Extract the term being defined (usually before "is", "refers", etc.)
                    words = word_tokenize(sentence)
                    if len(words) > 3:
                        # Simple heuristic: the term is usually at the beginning
                        term = ' '.join(words[:3])
                        definition_sentences.append((term, sentence))
                    break
        
        for term, sentence in definition_sentences[:num_questions]:
            # Create fake definitions for distractors
            fake_definitions = [
                "A completely different concept",
                "An unrelated technical term",
                "A misleading description",
                "An opposite meaning"
            ]
            
            # Extract actual definition (text after definition word)
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
    
    def process_pdf(self, pdf_path, num_questions=15):
        """Main method to process PDF and generate questions"""
        print("Extracting text from PDF...")
        raw_text = self.extract_text_from_pdf(pdf_path)
        
        if not raw_text:
            print("No text extracted from PDF.")
            return []
        
        print("Preprocessing text...")
        clean_text = self.preprocess_text(raw_text)
        
        print("Extracting key phrases...")
        key_phrases = self.extract_key_phrases(clean_text)
        
        print("Finding relevant sentences...")
        phrase_sentences = self.find_sentences_with_phrases(clean_text, key_phrases)
        
        print("Generating multiple choice questions...")
        mc_questions = self.generate_multiple_choice_questions(phrase_sentences, num_questions//2)
        
        print("Generating definition questions...")
        def_questions = self.generate_definition_questions(clean_text, num_questions//2)
        
        all_questions = mc_questions + def_questions
        random.shuffle(all_questions)
        
        return all_questions[:num_questions]
    
    def display_questions(self, questions):
        """Display generated questions in a formatted way"""
        for i, q in enumerate(questions, 1):
            print(f"\n{i}. {q['question']}")
            for j, option in enumerate(q['options']):
                print(f"   {chr(65+j)}. {option}")
            print(f"   Correct Answer: {chr(65 + q['correct_answer'])}")
            
            if 'target_phrase' in q:
                print(f"   Target: {q['target_phrase']}")

def main():
    # Initialize the question generator
    generator = PDFQuestionGenerator()
    
    # Specify your PDF file path
    pdf_file_path = "sample.pdf"  # Change this to your PDF file path
    
    try:
        # Generate questions
        questions = generator.process_pdf(pdf_file_path, num_questions=10)
        
        if questions:
            print("\n" + "="*60)
            print("GENERATED MULTIPLE CHOICE QUESTIONS")
            print("="*60)
            generator.display_questions(questions)
            
            # Save to file
            with open("generated_questions.txt", "w", encoding="utf-8") as f:
                f.write("Generated Multiple Choice Questions\n")
                f.write("="*50 + "\n\n")
                for i, q in enumerate(questions, 1):
                    f.write(f"{i}. {q['question']}\n")
                    for j, option in enumerate(q['options']):
                        f.write(f"   {chr(65+j)}. {option}\n")
                    f.write(f"   Correct Answer: {chr(65 + q['correct_answer'])}\n\n")
            
            print(f"\nQuestions saved to 'generated_questions.txt'")
        else:
            print("No questions could be generated from the PDF.")
            
    except FileNotFoundError:
        print(f"PDF file '{pdf_file_path}' not found.")
        print("Please make sure the file exists and update the 'pdf_file_path' variable.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()