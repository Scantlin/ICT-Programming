import sqlite3
import pandas as pd
import math
import sympy as sp

class Main:
    def __init__(self):
        self.answer = []
        self.equations = []

    def sql(self):
        #set = sqlite3.connect('Resistor_Pattter.db')
        #edit = set.cursor()

        data = pd.read_csv('Resistor_Pattern.csv')
        #print(data.isnull().sum().sum()) <- total null input in the data

        #edit.execute('CREATE TABLE resistors(Color TEXT, Digits INT, Multiplier INT, Tolerance TEXT)')
        #read = pd.read_sql('SELECT * FROM resistors', set)
        #read.to_csv('Resistor_Pattern.csv', index=False)
        query = 'INSERT INTO resistors (Color, Digits, Multiplier, Tolerance) VALUES (?,?,?,?)'

        #with set:
        #set.execute(query, ('silver', None, 0.01, '10%'))

        #set.commit()
        #edit.close()

        print('Successful')

    def equation(self):
        print('List of Tools \n1. Find x\n2. Derivatives \n3. Resistor Calculator \n4. Current Solver\n5. Integration Calculator\n6. Marginal Revenue\n7. Exit')
        choices = int(input('Enter your choice: '))

        options = {
            1: (self.express, True),
            2: (self.derivatives, True),
            3: (self.resistor, True),
            4: (self.current_solver, True),
            5: (self.integration, True),
            6: (self.marginal, True),
            7: (None, False),
        }

        actions, should_continue = options.get(choices, (self.invalid, True))

        if actions:
            actions()
        return should_continue

        '''
        if choices == 1:
            self.express()
        elif choices == 2:
            return False
        else:
            self.invalid()
        
        return True'''

    def derivatives(self):
        print('---------------------------- DERIVATIVES CALCULATOR ----------------------------')
        expression = input('Enter your expression: ')
        expression = sp.parse_expr(expression, transformations='all')
        print(f'Derivatives: {str(sp.diff(expression)).replace("**", "^").replace("*", "")}')
        print('---------------------------- THANK YOU ----------------------------')
        
    def express(self):
        print('---------------------------- FINDING X ----------------------------')
        equation = input('Enter your equation: ')
        x = sp.symbols('x') #to define x in the expression
        Equation_parse = sp.parse_expr(equation, transformations='all')
        answer = sp.solve(Equation_parse, x)
        print('the answer is',  ' and '.join(map(str, answer)))

        #Storingd data
        self.answer.append(', '.join(map(str, answer)))
        self.equations.append(equation)
        print('---------------------------- THANK YOU ----------------------------')

    def integration(self):
        print('---------------------------- INTEGRATION CALCULATOR ----------------------------')
        function = input('Enter your function: ')
        sparse_function = sp.parse_expr(function, transformations='all')
        print(f'Integrated Function: {str(sp.integrate(sparse_function)).replace('**', '^').replace('*', '')}')

        print('---------------------------- THANK YOU ----------------------------')

    def marginal(self):
        print('---------------------------- Marginal Revenue ----------------------------')
        function = input('Enter your function: ')
        units = int(input('Enter the units: '))
        sparse_function = sp.parse_expr(function, transformations='all') #transform the input function into python's operation system
        derivation = sp.diff(sparse_function, x) #Derivation
        substitution = sp.lambdify(x, derivation) #link the derivation value into the lamdify to substitute the inputted units
        print(f'Marginal Cost: {substitution(units)}') #see the output which is the cost

        print('---------------------------- THANK YOU ----------------------------')


    def resistor(self):
        print('---------------------------- RESISTOR CALCULATOR ----------------------------')
        data = pd.read_csv('Resistor_Pattern.csv')
        #print(data)

        data_dict = dict(zip(data['Color'], zip(data['Digits'] ,data['Multiplier'], data['Tolerance'])))

        num_band = int(input('Enter how many Bond: '))
        continuation = math.ceil(num_band/2)

        colors_bond = []

        init_count = 0

        while init_count < num_band:
            color = input(f'{init_count+1}: ').lower()
            if color in data['Color'].values:
                colors_bond.append(color)
                init_count += 1
            else:
                print('Invalid input')

        print(colors_bond)

        digits = ''
        for i, value in enumerate(colors_bond, start=1):
            if not pd.isna(data_dict[value][0]):
                digits += str(int(data_dict[value][0]))
                if i == continuation:
                    break
            else:
                continue

        if not pd.isna(data_dict[colors_bond[continuation]][1]):
            multiplier = data_dict[colors_bond[continuation]][1]
            print((int(digits) * int(multiplier)), 'Ohm')
        else:
            print(digits)

        if not pd.isna(data_dict[colors_bond[-1]][2]):
            print(data_dict[colors_bond[-1]][2], 'Tolerance')
        else:
            print('No tolerance')

        print('---------------------------- THANK YOU ----------------------------')

    def current_solver(self):
        print('---------------------------- CURRENT SOLVER ----------------------------')
    
        Holder = []
        Charge = '0'
        Time = '0'
        Current = '0'

        print('Choose Type \n1. Given the Value \n2. Problem Type')

        while True:
            choice = int(input('Enter your choice: '))
            if choice == 2:
                Problem = input('Enter your problem: ').replace(',', '').split(" ") #Give us a list content

                for i in range(len(Problem)):
                    if (any(c.isalpha() for c in Problem[i]) and any(c.isdigit() for c in Problem[i])):
                        if Problem[i].upper().endswith('C'): #to get charge <- Coulombs
                            Charge = Problem[i][:-1]
                        elif Problem[i].upper().endswith('M'): #for minutes
                            Time = eval(Problem[i][:-1] + '* 60')
                        elif Problem[i].upper().endswith('S'): #for seconds
                            Time = Problem[i][:-1]
                        elif Problem[i].upper().endswith('A'): #for current A <- Ampere
                            Current = Problem[i][:-1]
                break

            elif choice == 1:
                print('type \'x\' if that is the missing')
                Charge = input('Enter the charge (coulombs): ').replace('x', '0')
                Time = input('Enter the time (second): ').replace('x', '0')
                Current = input('Enter the current (Ampere): ').replace('x', '0')
                break

            else:
                print('Invalid Input')

        for i in range(1):
            Holder.append(Charge)
            Holder.append(Time)
            Holder.append(Current)

        for i, value in enumerate(Holder, start=1):
            if value == '0':
                formula = i
                break

        Holder = list(map(float, Holder))

        match formula:
            case 1: #Charge
                Holder[0] = Holder[1] * Holder[2]
                print(f'Charge: {round(Holder[0])} C')
            case 2: #Time
                Holder[1] = Holder[0]/Holder[2]
                print(f'Time: {round(Holder[1])} s')
            case 3: #Current
                Holder[2] = Holder[0]/Holder[1]
                print(f'Current: {round(Holder[2])} A')

        print('---------------------------- THANK YOU ----------------------------')
        

    def invalid(self):
        print('You input invalid option')

if __name__ == '__main__':
    app = Main() 
    try:
        running = True
        while running:
            running = app.equation()
        
        print('Thank you for using the program')

        #for i, value in enumerate(app.equations, start=0):
        #    print(f'Equation: {value} \nAnswer: {app.answer[i]}')

    except KeyboardInterrupt:
        print('Thank you for using the program')
        raise SystemExit