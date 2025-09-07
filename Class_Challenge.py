import sympy as sp
import pubchempy as pcp 
from flask import request
import math as mt
import numpy as np
import time

def show(list_song:list):
    for i in range(len(list_song)):
        print(list_song[i]," -> ", end="")
    print("null")

def singly():
    songs = []

    songs.append("Golden")
    songs.append("Got to believe")
    songs.append("Multo")
    
    print("Before adding Song 4")
    show(songs)

    print("After adding Song 4")
    songs.append("Naalala ka")
    show(songs)

    print("Deleting song 2")
    songs.remove(songs[1])
    show(songs)

singly()


information = {
    "John Scantlin B Cayson": 0.3,
    "1st year College": 0.3
}

for key, value in information.items():
    for char in key:
        print(char, end="", flush=True)
        time.sleep(value)
    print()

def divisor(number):
    divisor = []
    for i in range(1, number+1):
        if number % i == 0:
            divisor.append(i)
    return divisor

print(divisor(12))

def intersect2(interval, interval2):
    start = max(interval[0], interval2[0])
    end = min(interval[1], interval2[1])

    if start <= end:
        return [start, end]

print(intersect2([1, 5], [3, 7]))

def intersect_intervals(interval1:list, interval2:list):
    counting1 = []
    counting2 = []
    intersect = sorted([])
    for i in range(interval1[0], interval1[-1]+1):
        counting1.append(i)
    for i in range(interval2[0], interval2[-1]+1):
        counting2.append(i)
    
    for i in range(len(interval1)):
        if interval1[i] in counting2:
            intersect.append(interval1[i])
        if interval2[i] in counting1:
            intersect.append(interval2[i])
    
    return intersect

print(intersect_intervals([1, 5], [3, 7]))

def type_with_broken_keyboard(word):
    word = word.lower()
    a = ''
    b = 1
    for i in range(len(word)):
        if word[i] in 'aeiou':
            b += 1
        if b % 2 == 0:
            a += word[i].upper()
        else:
            a += word[i].lower()
    
    return a
    
print(type_with_broken_keyboard('banana'))

def reverse_odd_words(sentence):
    sentence = sentence.split(' ')

    sentence = sentence[::-1]

    return sentence

print(reverse_odd_words('Hello world this is a test'))

number = 117
primes = []

max_divisor = int(number**(1/2)) + 1

if number%2 == 0:
    primes.append(2)
    number = number//2

i = 3
while i <= max_divisor:
    if number % i == 0:
        primes.append(i)
        number = number // i
        max_divisor = int(number**0.5) + 1
    else:
        i += 2

if number > 1:
    primes.append(number)

# i = 3
# while i <= max_divisor:
#     while number % i == 0:
#         primes.append(i)
#         number = number // i
#         max_divisor = int(number**0.5) + 1
#     i += 2

# if number > 1:
#     primes.append(number)

print(primes)

def is_number_pandigital(num):
    return [str(n) in str(num) for n in range(10)]

print([n for n in range(5)])

def pandigital(int1):
    base = '0123456789'
    num = str(int1)

    if len(num) > 10:
        try:
            base = sorted(base * (len(num)//10))
        except Exception as e:
            return False

    answer = ''.join(base)
    inputted_number = sorted(list(num))
    check = ''.join(inputted_number)

    if answer == base:
        return True
    else:
        return False

print(pandigital(12345678901234567890))

def are_buddy_sring(str1:str, str2:str):
    if str2 == str1:
        return False
    else:
        str2 = list(str2)
        first = str1[0]
        second = str1[1]

        for i in range(2):
            str2.pop(0)
    
        str2.insert(0, first)
        str2.insert(1, second)

        word = ''.join(str2)

        if word == str1:
            return True
        else:
            return False

print(are_buddy_sring('hello', 'ohell'))
def spongecase(word:str):
    word = word.lower()
    sponge = []
    word = list(map(str, word))
    non_space = 0

    if ' ' in word:
        pass
    else:
        word.insert(0, '')
    
    for char in word:
        if char.isspace():
            sponge.append(char)
        else:
            if non_space % 2 == 0:
                sponge.append(char.upper())
            else:
                sponge.append(char.lower())
        non_space += 1

    return ''.join(sponge)

print(spongecase('python you and me'))

def euclid_mullin(n):
    sequence = []
    product = 1  # Initialize product of previous terms
    
    for _ in range(n):
        candidate = product + 1
        next_term = smallest_prime_factor(candidate)
        
        sequence.append(next_term)
        product *= next_term  # Update product
    
    return sequence

def smallest_prime_factor(n):
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return d
    return n  # n itself is prime if no divisor found

# Example: Generate first 10 terms
print(euclid_mullin(10))

def largest_prime_factor(n):
    largest = 1
    
    # Divide by 2 until n is odd
    while n % 2 == 0:
        largest = 2
        n = n // 2
    
    # Now check odd divisors up to sqrt(n)
    i = 3
    max_factor = int(n**0.5) + 1
    while i <= max_factor:
        while n % i == 0:
            largest = i
            n = n // i
            max_factor = int(n**0.5) + 1  # Update max factor
        i += 2
    
    # If remaining n is a prime > 2
    if n > 2:
        largest = n
    
    return largest
# x = ['Scantlin', 'B', 'Cayson']
# print(sorted(x, key=lambda c:(len(c), c)))
# def ginortS(s):
#   return ''.join(sorted(s, key=lambda c:(c.isdigit() - c.islower(), c in '02468', c)))

# print(ginortS('Hackathon2021'))

def sorting(s:str):
    sorting = []
    number = []
    number_odd = []
    number_even = []

    for i in range(len(s)):
        if s[i].islower():
            sorting.append(s[i])
    sorting = sorted(sorting)
    for i in range(len(s)):
        if s[i].isupper():
            sorting.append(s[i])
    for i in range(len(s)):
        if s[i].isnumeric():
            number.append(s[i])
    numbers_check = list(map(int, number))

    for i in range(len(numbers_check)):
        if numbers_check[i] % 2 != 0 and numbers_check[i] != 0:
            number_odd.append(str(numbers_check[i]))
    
    for i in range(len(numbers_check)):
        if numbers_check[i] % 2 == 0:
            number_even.append(str(numbers_check[i]))
    
    number_even = sorted(number_even)
    
    output = sorting + number_odd  + number_even

    return ''.join(output)

print(sorting('Hackathon2021'))

# user_choice = input('enter chosen pet: ')
# choices = {
#     'dog':'Arf',
#     'cat': 'meow',
# }

# choice = choices.get(user_choice, 'invalid')
# print(choice)

# class MyDog:
#     def __init__(self, name):
#         self.name = name

#     def show_my_dog_name(self):
#         return f'my Dog name is {self.name}'

# x = MyDog('Hershey')
# print(x.show_my_dog_name())
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