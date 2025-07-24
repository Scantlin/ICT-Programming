#this is compilation of the daily activities
from math import pi
from sympy import diff, symbols
import pandas as pd
import sqlite3
import random
import sympy as sp

#Challenge 1
def C1(degree) -> float:
    radians = (degree * pi/180)
    return round(radians, 3)

#Challenge 2
def C2(number, mode):
    if mode == 'asc' or mode == '1':
        number.sort()
        return ', '.join(map(str, number))
    elif mode == 'desc' or mode == '2':
        number.sort(reverse=True)
        return ', '.join(map(str, number))
    elif mode == 'none' or mode == '3':
        return ', '.join(map(str, number))
    else:
        return 'input a valid command'

#Challenge 3
def C3(decimal):
    init = decimal
    binary = []

    for i in range(9):
        if decimal % 2 == 0:
            binary.append(0)
        elif decimal % 2 == 1:
            binary.append(1)

        decimal = decimal // 2

    binary.reverse()
    binary_list = ''.join(map(str, binary))

    return binary_list.lstrip('0') #lstrip() method remove the character at first rtrip() remove the characted in the end

#Challenge 4
def C4(Binary):
    init = list(map(int, Binary))
    max_divior = 256
    decimal = 0

    for i in range(len(Binary)):
        init[i] *= max_divior
        max_divior = max_divior//2
        decimal += init[i]

    return decimal

#Challenge 5
def C5(func: str, unit: int):
    x = symbols('x')
    function = func.replace('x', '*x').replace('^', '**').replace(' *x', ' x')
    derive = diff(function)

    #Method 1
    def f(x):
        return eval(str(derive))
    return f(unit)

    #Method 2
    '''
    ev = lambda uni: derive.subs(x, uni)
    print(ev(unit))'''

#Challenge 6
def C6(name1:str, name2:str, ov_len:int):
    your_name1 = name1.lower()
    crush_name = name2.lower()
    
    for i in your_name1:
        if i in crush_name:
            your_name1 = your_name1.replace(i, '')
            crush_name = crush_name.replace(i, '')

    print(f'number of similar letter: {ov_len - len(your_name1 + crush_name)}')

#Challenge 7
def C7():
    set = sqlite3.connect('Flames.db')
    data = pd.read_sql('SELECT * FROM users', set)

    print(data)

#Challenge 8
def C8(num_list:list, Choice:int):

    match Choice:
        case 1:
            return "squared:", list(map(lambda x: x**2, num_list))
        case 2:
            return "summation:", sum(num_list)
        case 3:
            return "Mean:", sum(num_list)/len(num_list)

#Challenge 9
def C9(choice:int):
    con = [5]
    command = {
        1: ('Scant', 'Nathan'),
        2: ('You', 'me'),
        3: ('Done', 'Hope'),
        4: (None, 'Done')
    }

    name, partner = command.get(choice, ('invalid', 'not sure'))
    #print(f'name: {name}')
    #print(f'partner: {partner}')

    if con: #If it contains something particulary uses in list, array or tuple
        print(name)
        print(partner)
    else:
        print(partner)


#Challenge 10
def C10():
    data = pd.read_csv('general_knowledge.csv')
    
    data_dict = dict(zip(data['question'], data['answer']))

    data_dict_list = {key: value.lower().replace('of', "").split() for key, value in data_dict.items()}

    list_question = list(data_dict.keys())
    random.shuffle(list_question)

    x = 1
    score = 0
  
    for i in list_question:
        print(f'{x}, {i}')
        answer = input('Answer: ').strip().lower()

        if answer in data_dict_list[i]:
            print('Correct')
            score += 1
        
        else:
            print('wrong')
            print('correct answer: ', data_dict[i])

        x += 1

        if x == 6:
            print(f'Your score is {score}/{x-1}')
            print('Thank you for playing')
            break

#Challenge 11
def C11(equa:str, answer):
    x = symbols('x')
    parse = sp.parse_expr(equa, transformations='all')
    Equation = sp.Eq(parse, answer)

    ans = sp.solve(Equation, x)
    print('Answer:', ' and '.join(map(str, ans)))

if __name__ == '__main__':
    #C1 Convert degree to radians
    '''deg = int(input('Enter the degree: '))
    print(C1(deg), 'rad')'''

    #C2 Accept list and sort it depends on the user prefer mode
    '''
    length = int(input('Enter the length of the list: '))
    print('Enter the numbers: ')
    list_num = []

    for i in range(length):
        num = int(input())
        list_num.append(num)

    print('Enter the mode \n1. asc \n2. desc \n3. None')
    modes = input('Choice: ').lower()

    print(C2(list_num, modes))'''

    #C3 Convert Decimal to binary and Vice Versa
    '''
    dec = int(input('Enter your decimal: '))
    print(f'Binary: {C3(dec)}')
    print(f'check: {bin(dec)[2:]}')'''

    #C4 Convert Binary into Decimal
    '''
    print('-------Enter 8bit binary-------')
    bina = input('Enter your Binary in 8bit: ')
    if len(bina) != 9:
        print(f'invalid input, make sure it is 8bit binary, you inputted {len(bina)} character')
    else:
        print(f'Decimal of {int(bina)}: {C4(bina)}')'''

    #C5 Marginal Revenue
    '''fun = input('Enter your function: ').strip()
    Unit = int(input('Enter the unit: '))

    print(f'Marginal cost is {C5(fun, Unit)}')'''

    #return the number of similar letter in two words
    '''
    name = input('Your name: ').replace('.', '')
    crush = input('Crush name: ').replace('.', '')
    combine_len = len(name + crush)

    C6(name, crush, combine_len)'''

    #print the dataframe
    #C7()

    #return the squared value on a list, when the user input the numbers
    '''
    nums = []

    print('Operations: \n1. Squared\n2. Sum\n3. Mean')
    choice_user = int(input('Enter your choice: '))

    if choice_user > 3 or choice_user <= 0:
        print('Invalid Input')
    else:
        length = int(input('Enter how many digits you will enter: '))
        print('Enter your numbers: ')

        for i in range(length):
            num = int(input())
            nums.append(num)

        result = C8(nums, choice_user)
        print(f'result for {result[0]} {result[1]}')'''

    #Get function in dictionary
    choice = int(input('Enter a number from 1 - 3: '))
    C9(choice)

    #C10()

    #Finding X from an equation
    '''
    user_input_ex = input('Enter your expression: ')
    answer_user = int(input('Enter the answer: '))
    
    C11(user_input_ex, answer_user)'''