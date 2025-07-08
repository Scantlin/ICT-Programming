def main():
    length = int(input('Enter the length of the fibonacci sequence: '))
    fibo = [1, 1]

    for i in range(length-2):
        add = fibo[-1] + fibo[-2]
        fibo.append(add)

    print('Fibonacci Sequence is: ' + ', '.join(map(str,fibo)))

if __name__ == '__main__':
    main()