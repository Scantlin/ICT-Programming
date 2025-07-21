import sqlite3
import pandas as pd
from datetime import datetime
import pytz
import random

class Main:
    def __init__(self, users:str):
        self.users = users
        self.pytz = pytz.timezone('Asia/Manila')
        self.date = datetime.now(self.pytz).strftime('%d-%m-%y %H:%M')
        
        print('--------------------------------------------------------------------')
        print(f'You played the game on {self.date} name: {self.users}')

        self.questions = {
            'What is the largest planet on the solar system?': ['jupiter'],
            'What is 5x5 equal to?': ['25'],
            'what is the highest mountain on the world?': ['mt. everest', 'everest'],
            'Who is the father of Accounting?': ['luca pacioli', 'pacioli'],
            'What is the derivatives of sin?': ['cos'],
            'What is the largest river in the world?': ['nile', 'nile river'],
            'What is the game': ['none']
        }
    
        self.score = 0 #initialize the score into zero
        self.keys = list(self.questions.keys())

        print('QUIZ menu\n1. Start\n2. Show Score\n3. Exit')

    def show_menu(self):
        choice = int(input("Enter Choice: "))

        #METHOD 1 for dictionary
        command = {
            1: (self.display_question, True),
            2: (self.show_score, True),
            3: (None, False)
        }
        action, should_continue = command.get(choice, (self.invalid, True))
        
        if action:
            action()
        return should_continue

        #METHOD 2 for if-else statement
        '''
        if choice == 1:
            self.display_question()
        elif choice == 2:
            self.show_score()
        elif choice == 3:
            print('exiting the menu...')
            return False
        else:
            self.invalid()
        
        return True''' #Default True value, despite what will you choose except 3, the menu program will still continue

    def invalid(self): #if user input the invalid program
        print('Invalid input, Please Try Again')

    #a method to display questions and get the answer from the user
    def display_question(self):
        self.score = 0
        '''
        for key, value in (self.questions.items()):
            print(key)
            answer = input('Answer: ').strip().lower()'''

        random.shuffle(self.keys)

        '''shuffled_dict = {k: self.questions[k] for k in self.keys}
        print(shuffled_dict)'''

        for key in self.keys:
            print(key)
            answer = input('Enter your answer: ').strip().lower()
            if answer in self.questions[key]:
                self.score += 1
   
        if self.score == len(self.questions):
            print(f'CONGRATULATIONS {self.users.upper()} YOU GOT A PERFECT SCORE')
        else:
            print(f'{self.users.upper()}\'s Score: {self.score}/{len(self.questions)}')

        self.database(self.users, self.score, self.date) #always call the function database to update the database itself'''
    
    def show_score(self):
        print(f'{self.users}\'s Current Score: {self.score}')

    def database(self, name:str, score:int, date:str): #The Database
        set_connect = sqlite3.connect('Class_quiz_scores.db')
        edit = set_connect.cursor()

        #edit.execute('CREATE TABLE users(Name TEXT, Score INT, Date TEXT)')
        #edit.execute('DROP TABLE users')

        query = 'INSERT INTO users(Name, Score, Date) VALUES(?, ?, ?)'

        with set_connect:
            set_connect.execute(query, (name, score, date))

        read_data = pd.read_sql('SELECT * FROM users', set_connect)
        read_data.to_csv('Class_quiz_scores.csv', index=False)

        set_connect.commit()
        edit.close()

if __name__ == '__main__':
    try:
        game = True
        while game: #looping the main program
            user = input('Enter your name: ')
            app = Main(user)

            playing = True #for the looping of the game program
            while playing:
                playing = app.show_menu()

            validate = True #to make sure that the user will input only valid program
            while validate:
                choice = input('You want to play another game? (Y/n): ').lower().strip()

                if choice == 'y':
                    validate = False
                elif choice == 'n':
                    validate = False
                    game = False
                    print('Thank you using the program')
                else:
                    print('invalid input')
                    pass

    except KeyboardInterrupt:
        print('Thank you for playing')
        raise SystemExit
