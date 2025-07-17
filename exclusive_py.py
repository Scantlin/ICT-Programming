import time

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = round(time.time() - t1, 5)
        print(func.__name__, 'is', t2, 'seconds')
    return wrapper

@tictoc
def exceute_this():
    print(time.sleep(2))

def second_execution():
    time.sleep(2)

exceute_this()
#second_execution()
print('Done')

#DECORATORS
def add_sprinkles(func): #-> a function decorator
    def wrapper(*args, **kwargs): #-> a function inside a function

        print(f'you added a sprinkles to your {args[0]} ice cream')
        func(*args, **kwargs) #-> if there is no function call, then it just execute the print above, and not the function that passed on the decorators function
        #*args is for any arguments, and **kwargs is for keywor
    return wrapper

@add_sprinkles #-> decorators @ and the name of the function decorator
def get_ice_cream(flavor):
    print(f'here is your {flavor} ice cream')

#flavor = input('enter your flavor: ').capitalize()
get_ice_cream('chocolate')
#second_ice_cream()

#**KWARGS AND *ARGS
def sample(*size, **details):
    for size in size:
        print(size)

    for key, value in details.items():
        print(f'{key}: {value}')

sample('small', 'medium', 'large', tip=5, delivery=True)

'''
def timer(func):
    def wrapper(*args, **kwargs):
        for i in range(1, int(args[0]) + 1):
            print(f'progress {i}/{args[0]}', end='\r')
            time.sleep(1)
        func(*args, **kwargs)
    return wrapper

@timer
def count(times:int):
    print('\nDone Execution of your timer')

def get_time() -> str:
    timezone = tz('Asia/Manila')

    now: datetime = datetime.now(timezone)
    return f'{now:%X}

def main():
    length = int(input('Enter the length of the diamond: '))
    for i in range(1, length+1):
        print(' ' * ((length+1)-i), '* ' * i//2)

    for j in range(length+1, 0, -1): #start, end, step
        print(' ' * ((length+1)-j), '* ' * j//2)
if __name__ == '__main__':
    main()'''