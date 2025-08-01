import sympy as sp
import pubchempy as pcp
import requests

print('-------------------Arithmetic Sequence----------------------------')
choice = int(input('1. Arithmetic Sequence \n2. Geometric Sequence \nChoice: '))
missing = int(input('Enter number of missing: '))
Ar_sequence_string = input('Enter sequence: ').replace(',', ' ').split(' ') #string first to apply the aplit function
Ar_sequence_string = list(map(int, Ar_sequence_string))

if choice == 1:
    cd = Ar_sequence_string[1] - Ar_sequence_string[0]
    for i in range(missing):
        val = Ar_sequence_string[-1] + cd
        Ar_sequence_string.append(val)

    Ar_sequence_string = list(map(str, Ar_sequence_string))
    print('Arithmetic Sequence:', ', '.join(Ar_sequence_string))

elif choice == 2:
    CR = Ar_sequence_string[1]/Ar_sequence_string[0]
    for i in range(missing):
        val = Ar_sequence_string[-1] * CR
        Ar_sequence_string.append(val)

    Ar_sequence_string = list(map(str, Ar_sequence_string))
    print('Geometric Sequence:', ', '.join(Ar_sequence_string))

else:
    print('invalid input')

    

#sample API
'''
api_url = "http://api.weatherapi.com/v1/current.json?key=9daec57f4f154f2bb71133330250108&q=Philippines&aqi=yes"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print('data successfully retrieve')
    print(data)
    print(data['location'])
    print(data['current']['wind_degree'])
    print(data['current'].keys())

else:
    print(f'Error: {response.status_code} - {response.text}')
'''
'''
chemical_name = input("Enter your chemical name: ")
compound = pcp.get_compounds(chemical_name, 'name')[0]

print(f'IUPAC name: {compound.iupac_name}')
print(f'exact mass: {compound.exact_mass}')
print(f'molecular formula: {compound.molecular_formula}')
print(f'{compound}')
'''
'''
x = sp.Symbol('x')
func = input('Enter function: ')
print(sp.Derivative(func, x, evaluate=True))
'''

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