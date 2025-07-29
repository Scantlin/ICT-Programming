import sympy as sp

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