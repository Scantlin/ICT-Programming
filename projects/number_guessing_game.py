import random

class number_guessing_game:
    def __init__(self):
        print("----- Welcome to Guessing Game -----")
        self.number = random.randint(0, 10)
        self.conti = True
    
    def play(self, guess):
        self.guess = guess
        if self.guess == self.number:
            print("You guessed it right!")
            self.conti = False
        elif self.guess > self.number and self.guess <= self.number:
            print("lower your guess")
        elif self.guess < self.number and self.guess > 0:
            print("higher your guess")
        else:
            print("You input invalid number")

        return self.conti
        
if __name__ == "__main__":
    game = number_guessing_game()
    playing = True
    while playing:
        guess_input = int(input("Enter your guess: "))
        playing = game.play(guess_input)