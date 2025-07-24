import sympy as sp

class Main:
    def __init__(self):
        self.answer = []
        self.equations = []

    def equation(self):
        print('Options\n1. Find x\n2. Exit')
        choices = int(input('Enter your choice: '))

        options = {
            1: (self.express, True),
            2: (None, False)
        }

        actions, should_continue = options.get(choices, (self.invalid, True))

        if actions:
            actions()
        else:
            if should_continue == False:
                print('Thank you for using the app')
            return should_continue
        

    def express(self):
        equation = input('Enter your equation: ')
        x = sp.symbols('x') #to define x in the expression
        Equation_parse = sp.parse_expr(equation, transformations='all')
        answer = sp.solve(Equation_parse, x)
        print('the answer is',  ' and '.join(map(str, answer)))

        #Storingd data
        self.answer.append(answer)
        self.equations.append(equation)

    def invalid(self):
        print('You input invalid option')

if __name__ == '__main__':
    app = Main() 

    running = True
    while running:
        running = app.equation()

    for i, value in enumerate(app.equations):
        print(f'Equation: {value} \nAnswer: {app.answer[i]}')



'''
def C11(equa: str, answer:int):
    x = sp.symbols('x')
    Equ_par = sp.parse_expr(equa, transformations='all')
    Equation = sp.Eq(Equ_par, answer)

    print(sp.solve(Equation, x))

C11("2x + 7x", 27)'''

'''
x = sp.symbols('x')
Equation = sp.Eq(x + 2, 5)

print(sp.solve(Equation, x))
'''
'''
a = np.array([2, 5, 6])
b = np.array([3, 4, -5]).reshape(-1, 1)

print('matrics A',a)
print('matrics B', b)
print(a @ b) #use @ to multipy to matrics according to rule
#or

print(np.matmul(a, b))
print(eval('x + 2 == 5'))
'''
'''
class Main:
    def __init__(self):
        self.data_name = []
        self.data_age = []
        self.data_school = []

    def school(self, name, age:int, school):
        self.data_name.append(name)
        self.data_age.append(age)
        self.data_school.append(school)
    
    def data(self):
        for num, val in enumerate(self.data_name, start=0):
            print(f'user #{num+1}')
            print(f'name: {val}')
            print(f'age: {self.data_age[num]}')
            print(f'school: {self.data_school[num]}')

if __name__ == '__main__':
    initialize = 1
    num_user = int(input('Enter how many users: '))
    main = Main()
    while initialize < num_user+1:
        try:
            print(f'user #{initialize}')
            name_user = input('Enter your name: ').capitalize().strip()
            age_user = int(input('Enter your age: '))
            school_user = input('Enter your school: ').capitalize()

            main.school(name_user, age_user, school_user)
            initialize += 1

        except KeyboardInterrupt:
            raise SystemExit

    main.data()'''