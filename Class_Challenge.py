import sympy as sp
import pubchempy as pcp 
from flask import request
import math as mt
import numpy as np

class MyDog:
    def __init__(self, name):
        self.name = name

    def show_my_dog_name(self):
        return f'my Dog name is {self.name}'

x = MyDog('Hershey')
print(x.show_my_dog_name())
# def check_email(emails:list):
#     add = []
#     #unique = 0

#     for i in range(len(emails)):
#         start = emails[i].find('@')
#         add.append(emails[i][start+1:])

#     unique = len(set(add))
#     print(unique)

# check_email(['asdsbc@gmail.com', 'xyz@yahoo.com', 'abc@gmail.com'])

# def check_both(n):
#     convert = str(n)
#     num = list(map(int, convert))
#     sum_num = sum(num)
#     if sum_num % 2 == 0 and n %2==0:
#         return True
#     elif sum_num %2 != 0 and n%2 != 0:
#         return True
#     else:
#         return False

# print(check_both(123))

# def check(dict1, word:str):
#     for key, value in dict1.items():
#         word = word.replace(key, value)

#     return word

# dictionary = {
#     "g":"b",
#     "o":"a",
#     'd':'y'
# }
# print(check(dictionary, 'goodbye'))
'''
def key_exists(dict1, key):
    print(key in dict1)

dictionary = eval(input('Enter your dictionary: '))
key_user = input('Enter the keys: ')

key_exists(dictionary, key_user)'''

# m = np.array([1, 2, 3, 4, 5, 2.0])
# y = list(map(int, m))

# for i in y:
#     if isinstance(i, int):
#         print(i + 7)

'''
for ind in range(len(y)):
    if y[ind].is_integer():
        y[ind] = int(y[ind])
print(y)'''

# print('-------------------Arithmetic Sequence----------------------------')
# choice = int(input('1. Arithmetic Sequence \n2. Geometric Sequence \nChoice: '))
# missing = int(input('Enter number of missing: '))
# Ar_sequence_string = input('Enter sequence: ').replace(',', ' ').split(' ') #string first to apply the aplit function
# Ar_sequence_string = list(map(int, Ar_sequence_string))

# if choice == 1:
#     cd = Ar_sequence_string[1] - Ar_sequence_string[0]
#     for i in range(missing):
#         val = Ar_sequence_string[-1] + cd
#         Ar_sequence_string.append(val)

#     Ar_sequence_string = list(map(str, Ar_sequence_string))
#     print('Arithmetic Sequence:', ', '.join(Ar_sequence_string))

# elif choice == 2:
#     CR = Ar_sequence_string[1]/Ar_sequence_string[0]
#     for i in range(missing): 
#         val = Ar_sequence_string[-1] * CR
#         Ar_sequence_string.append(val)

#     Ar_sequence_string = list(map(str, Ar_sequence_string))
#     print('Geometric Sequence:', ', '.join(Ar_sequence_string))
    
# else:
#     print('invalid input')

# def C12(nums:list[int]):
#     print(max(nums))
#     print(min(nums))

# C12([5, 3, 2, 1])

# x = ['scantlin', 12, 'STI COLLEGE CALAMBA']
# x.append('Nathaniel')
# x.append(19)
# x.remove(12)
# x.insert(1, 19)
# print(x)

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