from random import randint

class Dice_simulator:
    def __init__(self):
        print("Welcome to Dice Simulator")
        print("press any key to continue...")
        input() #initialize the user

        self.num = randint(1, 6)
    
    def roll(self, roll=False):
        if roll == True:
            print(f"your dice number: {self.num}")
        else:
            pass

if __name__ == '__main__':
    Dice_simulator().roll(roll=True)