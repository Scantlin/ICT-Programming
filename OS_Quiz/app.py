from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# File to store scores
SCORES_FILE = 'scores.json'

def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_scores(scores):
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    score = data.get('score')
    
    if not all([first_name, last_name, score is not None]):
        return jsonify({'error': 'Missing data'}), 400
    
    # Load existing scores
    scores = load_scores()
    
    # Add new score
    player_name = f"{first_name} {last_name}"
    scores.append({
        'name': player_name,
        'score': score
    })
    
    # Save updated scores
    save_scores(scores)
    
    return jsonify({'success': True})

@app.route('/get_leaderboard', methods=['GET'])
def get_leaderboard():
    scores = load_scores()
    
    # Sort by score (descending) and get top 3
    sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)
    top_scores = sorted_scores[:3]
    
    return jsonify(top_scores)

if __name__ == '__main__':
    app.run(debug=True)