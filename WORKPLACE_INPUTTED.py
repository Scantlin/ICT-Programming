print('---------------------------------------------------------------------------------------------------------------')
#THIS WORKPLACE IS FOR IMPROVING THE CODES FOR PYTHON
print('---------------------------------------------------------------------------------------------------------------')

print('---------------------------------------------------------------------------------------------------------------')
#DICTIONARY 
#-----------------------------------------------------------------------------------
def generate_dict(lyrics):
    mydict = {}
    for word in lyrics:
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1

    return mydict

sample_lyrics = ['you', 'love', 'me', 'mahal', 'kita', 'me', 'kita', 'love', 'love']
freq = max(generate_dict(sample_lyrics).values())

for key, value in generate_dict(sample_lyrics).items():
    if value == freq:
        print(f'{key} has the most frequency with {freq}')

#-----------------------------------------------------------------------------------
import pandas as pd

student = {
    'name': ['Scantlin', 'Emman', 'Dave', 'Vince'],
    'Grade': ['2nd year', '2nd year', '2nd year', '2nd year'],
    'sex': ['male', 'male', 'male', 'male'],
    'single': ['yes', 'no', 'no', 'yes']

}

print(student['name']) #access the value from the key in name
print('john' in student) #to check if it exist on the dictionary
print(student.values()) #return all the values in the student dictionary
print(student.keys()) #return all the keys in the student dictionary

df = pd.DataFrame(student) #convert the dictionary into dataframe
print(df)
del(student['single']) #to delete the key and value on the dictionary
print(student)

print('---------------------------------------------------------------------------------------------------------------')
#FIBONACCI SEQUENCE   
def main2():
    length = int(input('Enter the length of the fibonacci sequence: '))
    fibo = [1, 1]

    if length > 1:
        for i in range(length-2):
            add = fibo[-1] + fibo[-2]
            fibo.append(add)
        
        print('Fibonacci Sequence is: ' + ', '.join(map(str,fibo)))
        print(f'the sum of fibonacci sequence is: {sum(fibo)}')

    elif length == 0 or length < 0:
        print('invalid number')

    else:
        fibo.pop()
        print('only 1')

def main3(x):
    if x == 0 or x == 1:
        return 1

    else:
        return main3(x - 1) + main3(x - 2)


if __name__ == '__main__':
    print(main3(2))
    main2()

print('---------------------------------------------------------------------------------------------------------------')
#CHANGING 6 INTO 9
def main():
    number = input('Enter a number 6 and 9: ')

    initiator = list(map(int, number))

    for i in range(len(initiator)):
        if initiator[i] == 6:
            initiator[i] = 9
    
    num = ''.join(map(str, initiator))

    print(num)

main()
print('---------------------------------------------------------------------------------------------------------------')
#TUPLES AND ITS USES, SAMPLE CODE FROM MIT
def get_data(data):
    nums = ()
    words = ()

    for t in data:
        nums = nums + (t[0], )
        if t[1] not in words:
            words = words + (t[1], )

    min_val = min(nums)
    max_val = max(nums)
    unique = len(words)

    return (min_val, max_val, unique)

tuple_sample = ((1, "a", "scant"), (2, "b", "cayson"), (3, "b", "pogi"))
word = 'scantlin'

if 'n' not in word:
    print('not included')

L = [1, 2, 3, 6, 3, 4, 10, 100, 21, 89]

print('---------------------------------------------------------------------------------------------------------------')
#LINSPACE OF NUMPY AS A OWN WRITTEN CODE, RECURSION AND SELF MADE CODE

import numpy as np
#x = np.linspace(min(L), 50, 10)
#print(x)

def fact(x):
    if x == 1:
        return 1
    else:
        return x*fact(x-1)

print(fact(10))

def fact_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

print(fact_iter(10)) #this print the factorization of the number

def sample(a, b):
    if b == 1:
        return a

    else:
        return a + sample(a, b-1)

print(sample(3,10)) #this print the product of two numbers

def summation(a):
    if a == 1:
        return a

    else:
        return a + summation(a-1)

print(summation(100))

def summations(n):
    initiator =[]
    sum = 0
    for i in range(1, n+1):
        initiator.append(i)

    for i in range(n):
        sum += initiator[i]

    return sum

print(summations(100))

def linspace(start, stop, times):
    write = []
    start = start
    first = (stop - start)/(times-1)

    for i in range(times):
        write.append(start)
        start += first

    return write

print(linspace(2, 50, 7))

print(np.linspace(2, 50, 7))
print('---------------------------------------------------------------------------------------------------------------')
#INTERACTION BETWEEN DATE TIME AND HOW TO CALCULATE THE EXACT AGE

from datetime import datetime, date
import pytz 

timezone = pytz.timezone('Asia/Manila')

user = input("enter your birthday (yyyy-mm-dd): ")
x = user.split("-")
convert = list(map(int, x))

year = datetime(convert[0], convert[1], convert[2]).date()
current = datetime.now(timezone).date()

diff = current - year

print(round((diff).days/365.2425, 6), 'years')

print('---------------------------------------------------------------------------------------------------------------')
from datetime import datetime

def exact_age(birth_date, current_date=None):
    """Calculate exact age in years (including decimal precision)."""
    if current_date is None:
        current_date = datetime.now()
    delta = current_date - birth_date  # Time difference in days
    return delta.days / 365.2425  # Continuous age in years

# Example: Born on Dec 11, 2005, as of July 11, 2025
birth_date = datetime(2005, 12, 11)
current_date = datetime(2025, 7, 11)

age = exact_age(birth_date, current_date)
print(f"Exact age: {age:.6f} years")  # Output: 19.580822 years

print('---------------------------------------------------------------------------------------------------------------')
#JOINING STRING FROM A LIST

x = [1, 2, 3]
print(", ".join(map(str, x)))

print('---------------------------------------------------------------------------------------------------------------')
#QR CODE CONVERTER
import pyqrcode
import png

def main():
    url = 'https://comsimwave.netlify.app/' #input what you gonna convert into qrcode
    img = pyqrcode.create(url)
    img.png('qrcode_result.png', scale=8)

if __name__ == '__main__':
    main()

print('---------------------------------------------------------------------------------------------------------------')
#FACTORIAL

import math

def main():
    number = int(input('Enter a number: '))
    #create a initialization where we input the countings of a numbers from the user's number
    initialize = []
    #initialize the factorial variable with 1
    fact = 1

    #to store all the counting in our initialization
    for i in range(1, number+1):
        initialize.append(i)

    #this is where the process of factoring take place, when multiply the fact variable by indexing of initialization then assigned it
    for i in range(len(initialize)):
        fact *= initialize[i]

    #the print the output
    print(fact)

    #checking using the module of math
    print(math.factorial(number))
    
if __name__ == '__main__':
    main()

print('---------------------------------------------------------------------------------------------------------------')
#BASIC AUTHORIZATION

from random import randint

def main():
    code = randint(1000, 9999)
    print(f'Your code is {code}')
    user = int(input('Enter your Authorizattion: '))

    if code == user:
        print('Enter Successfully')
    else:
        print('Sorry Try again later')

if __name__ == '__main__':
    main()


print('---------------------------------------------------------------------------------------------------------------')

print('---------------------------------------------------------------------------------------------------------------')

print('---------------------------------------------------------------------------------------------------------------')