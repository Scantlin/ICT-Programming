def triangle(length:int, charac:str):
    if charac not in ["*", "p", "^"]:
        print("please provide correct character")
        return "Try"
    else:
        star = f" {charac}"
        space = " "

        #for upper Triangle
        for i in range(1, length, 2):
            print((space * (length-i)) + (star * i))

        #for lower Triangle
        if length % 2 == 0:
            for i in range(length-3, 0, -2):
                print((space * (length-i)) + (star * i))
        else:
            for i in range(length, 0, -2):
                print((space * (length-i)) + (star * i))

if __name__ == "__main__":
    while True:
        length = int(input("Enter the length: "))
        charac = input("What character {*, p, ^}: ")

        x = triangle(length, charac)

        if x == "Try":
            pass
        else:
            again = input("Do you want to try again the program (Y/N): ").upper()

            if again == "Y":
                pass
            else:
                print("Thank you for using the program")
                break