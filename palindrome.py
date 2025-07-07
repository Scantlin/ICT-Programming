def main():
    '''
    add = lambda x: x+5
    print(add(5))'''
    
    word = input('Enter a word to check if it is a palindrome: ')
    palindrome = []
    for i in range(1, len(word)+ 1):
        letter = word[-i]
        palindrome.append(letter)

    if ''.join(palindrome) == word:
        print('palindrome')

    else:
        print('not a palindrome')


if __name__ == '__main__':
    main()