import random

class number_guessing_game:
    def __init__(self):
        self.number = random.randint(0, 100)

if __name__ == "__main__":
    print(number_guessing_game().number)