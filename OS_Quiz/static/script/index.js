class QuizGame {
    constructor() {
        this.currentQuestion = 0;
        this.score = 0;
        this.playerName = '';
        this.questions = [
            {
                question: "What is the capital of France?",
                options: ["Paris", "London", "Berlin", "Madrid"],
                answer: 0
            },
            {
                question: "Which planet is known as the Red Planet?",
                options: ["Venus", "Mars", "Jupiter", "Saturn"],
                answer: 1
            },
            // Add 13 more questions here following the same format
            {
                question: "What is 2 + 2?",
                options: ["3", "4", "5", "6"],
                answer: 1
            },
            {
                question: "Which language is primarily used for web development?",
                options: ["Python", "JavaScript", "Java", "C++"],
                answer: 1
            },
            {
                question: "What is the largest ocean on Earth?",
                options: ["Atlantic", "Indian", "Arctic", "Pacific"],
                answer: 3
            },
            {
                question: "Who wrote 'Romeo and Juliet'?",
                options: ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
                answer: 1
            },
            {
                question: "What is the chemical symbol for gold?",
                options: ["Go", "Gd", "Au", "Ag"],
                answer: 2
            },
            {
                question: "Which is not a primary color?",
                options: ["Red", "Blue", "Green", "Yellow"],
                answer: 3
            },
            {
                question: "How many sides does a hexagon have?",
                options: ["5", "6", "7", "8"],
                answer: 1
            },
            {
                question: "What is the largest mammal?",
                options: ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                answer: 1
            },
            {
                question: "Which year did World War II end?",
                options: ["1943", "1944", "1945", "1946"],
                answer: 2
            },
            {
                question: "What is the hardest natural substance on Earth?",
                options: ["Gold", "Iron", "Diamond", "Platinum"],
                answer: 2
            },
            {
                question: "Which element has the chemical symbol 'O'?",
                options: ["Gold", "Oxygen", "Osmium", "Oganesson"],
                answer: 1
            },
            {
                question: "How many continents are there?",
                options: ["5", "6", "7", "8"],
                answer: 2
            },
            {
                question: "What is the largest desert in the world?",
                options: ["Sahara", "Gobi", "Antarctic", "Arabian"],
                answer: 2
            }
        ];
        
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        document.getElementById('userForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.startGame();
        });

        document.getElementById('nextButton').addEventListener('click', () => {
            this.nextQuestion();
        });

        document.getElementById('playAgainButton').addEventListener('click', () => {
            this.resetGame();
        });
    }

    startGame() {
        const firstName = document.getElementById('firstName').value;
        const lastName = document.getElementById('lastName').value;
        this.playerName = `${firstName} ${lastName}`;
        
        // Hide login, show quiz
        document.getElementById('loginSection').style.display = 'none';
        document.getElementById('quizSection').style.display = 'block';
        
        this.displayQuestion();
    }

    displayQuestion() {
        if (this.currentQuestion >= this.questions.length) {
            this.endGame();
            return;
        }

        const question = this.questions[this.currentQuestion];
        document.getElementById('question').textContent = question.question;
        
        const optionsContainer = document.getElementById('options');
        optionsContainer.innerHTML = '';
        
        question.options.forEach((option, index) => {
            const button = document.createElement('button');
            button.textContent = option;
            button.className = 'option-button';
            button.onclick = () => this.selectOption(index);
            optionsContainer.appendChild(button);
        });
        
        document.getElementById('score').textContent = this.score;
    }

    selectOption(selectedIndex) {
        const correctIndex = this.questions[this.currentQuestion].answer;
        const options = document.querySelectorAll('.option-button');
        
        options.forEach((button, index) => {
            if (index === correctIndex) {
                button.classList.add('correct');
            }
            if (index === selectedIndex && index !== correctIndex) {
                button.classList.add('incorrect');
            }
            button.disabled = true;
        });
        
        if (selectedIndex === correctIndex) {
            this.score++;
            document.getElementById('score').textContent = this.score;
        }
        
        document.getElementById('nextButton').disabled = false;
    }

    nextQuestion() {
        this.currentQuestion++;
        document.getElementById('nextButton').disabled = true;
        this.displayQuestion();
    }

    async endGame() {
        // Send score to backend
        try {
            const firstName = document.getElementById('firstName').value;
            const lastName = document.getElementById('lastName').value;
            
            const response = await fetch('/submit_score', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    firstName: firstName,
                    lastName: lastName,
                    score: this.score
                })
            });
            
            if (response.ok) {
                this.showLeaderboard();
            }
        } catch (error) {
            console.error('Error submitting score:', error);
            this.showLeaderboard(); // Still show leaderboard even if submission fails
        }
    }

    async showLeaderboard() {
        // Hide quiz, show leaderboard
        document.getElementById('quizSection').style.display = 'none';
        document.getElementById('leaderboardSection').style.display = 'block';
        
        // Get leaderboard data
        try {
            const response = await fetch('/get_leaderboard');
            const leaderboardData = await response.json();
            
            const leaderboard = document.getElementById('leaderboard');
            leaderboard.innerHTML = '';
            
            leaderboardData.forEach((player, index) => {
                const ranks = ['1st', '2nd', '3rd'];
                const item = document.createElement('div');
                item.className = 'leaderboard-item';
                item.innerHTML = `
                    <span class="rank">${ranks[index]}</span>
                    <span class="name">${player.name}</span>
                    <span class="score">${player.score}/15</span>
                `;
                leaderboard.appendChild(item);
            });
        } catch (error) {
            console.error('Error fetching leaderboard:', error);
        }
    }

    resetGame() {
        this.currentQuestion = 0;
        this.score = 0;
        
        // Hide leaderboard, show login
        document.getElementById('leaderboardSection').style.display = 'none';
        document.getElementById('loginSection').style.display = 'block';
        
        // Reset form
        document.getElementById('userForm').reset();
    }
}

// Initialize the game when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new QuizGame();
});