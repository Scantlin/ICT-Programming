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