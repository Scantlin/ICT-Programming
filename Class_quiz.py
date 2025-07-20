class Main:
    def __init__(self, users):
        self.users = users

        self.questions = {
            'What is the largest planet on the solar system?': ['jupiter'],
            'What is 5x5 equal to?': ['25'],
            'what is the highest mountain on the world?': ['mt. everest', 'everest'],
            'Who is the father of Accounting?': ['luca pacioli', 'pacioli'],
            'What is the derivatives of sin?': ['cos'],
        }
    
        self.score = 0 #initialize the score into zero
        self.answer = [] #storing of the answer

        self.display_question() #call to display function
    
    #a method to display questions and get the answer from the user
    def display_question(self):
        for i, key in enumerate(self.questions.keys(), start=1):
            print()
            print(i, key)
            self.answer.append((input('Enter your answer: ')).lower())

        self.check_answer() #after answering all the questions provided we will now call the method to check answer

    #To check answer
    def check_answer(self):
        for i, value in enumerate(self.questions.values()):
            if self.answer[i] in value:
                self.score += 1
        if self.score == len(self.questions):
            print('CONGRATULATIONS YOU GOT A PERFECT SCORE')
        else:
            print(f'Your score: {self.score}/{len(self.questions)}')
        
if __name__ == '__main__':
    try:
        repeat = True

        while repeat:
            user_input = input('Enter your name: ')
            start = Main(user_input)
            print('----------------------------------------------')

            print("Welcome to your game", start.users)

            asking = True
            while asking:
                choices = input('Do you want to play again (Y/n): ')

                match choices:
                    case 'Y':
                        asking = False
                        print()
                    case 'n':
                        asking = False
                        repeat = False
                        print('Thank you for playing')
                    case _:
                        print('invalid command')
                        print()
    except KeyboardInterrupt:
        print("Thank you for playing")
