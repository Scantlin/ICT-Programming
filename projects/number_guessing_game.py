import random

class number_guessing_game:
    def __init__(self):
        print("Welcome to Guessing Game")
        self.number = random.randint(0, 10)
    
    def play(self, guess):
        self.guess = guess
        if self.guess == self.number:
            print("You guessed it right!")
            return False
        else:
            print("not right")
            return True
        
if __name__ == "__main__":
    game = number_guessing_game()
    playing = True
    while playing:
        guess_input = int(input("Enter your guess: "))
        playing = game.play(guess_input)