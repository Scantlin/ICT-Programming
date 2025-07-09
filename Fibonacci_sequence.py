def main():
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


if __name__ == '__main__':
    main()