import random

class number_guessing_game:
    def __init__(self):
        print("Welcome to Guessing Game")
        self.number = random.randint(0, 10)
    
    def play(self, guess):
        print()

if __name__ == "__main__":
    game = number_guessing_game()