import random
import time

class number_guessing_game:
    def __init__(self):
        self.number = random.randint(0, 10)
        self.conti = True
    
    def clean_line(self, n=1):
        for _ in range(n):
            print("\033[A\033[2K", end="")
    
    def play(self):
        print("-----Welcome to Guessing Game-----")
        print("Number: _")
        self.guess = int(input("Your guess: "))

        if self.guess == self.number:
            print("You guessed it right!")
            self.conti = False
        elif self.guess > self.number and self.guess <= self.number:
            print("lower your guess")
        elif self.guess < self.number and self.guess > 0:
            print("higher your guess")
        else:
            print("You input invalid number")
        
        time.sleep(1)
        self.clean_line(4)
        return self.conti
        
if __name__ == "__main__":
    game = number_guessing_game()
    playing = True
    while playing:
        playing = game.play()