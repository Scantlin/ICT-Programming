#Basic Authorization
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