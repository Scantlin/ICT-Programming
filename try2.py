print("This is a simple Calculator")
print("---------------------------")
run = True
while run:
    num1 = int(input("Enter a 1st number: "))
    num2 = int(input("Enter a 2nd number: "))
    
    def sum(x, y):
        return x + y
    def subtraction(x, y):
        return x - y
    def division(x, y):
        return x/y
    def multiplication(x, y):
        return x * y
    
    print("\nChoose an option \n 1. Sum \n 2. Subtraction \n 3. quotient \n 4. product")
    choose = int(input("Enter your choice: "))
    def switch_match(choose):
        match choose:
            case 1:
                return (sum(num1, num2))
            case 2:
                return (subtraction(num1, num2))
            case 3:
                return (division(num1, num2))
            case 4:
                return (multiplication(num1, num2))
            case _:
                return "invalid input"
        print(switch_match(choose))
        
