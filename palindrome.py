def main():
    '''
    add = lambda x: x+5
    print(add(5))'''
    
    word = input('Enter a word to check if it is a palindrome: ')
    palindrome = [] #or just use the built in method of python list() to convert the string into list
    for i in range(1, len(word)+ 1):
        letter = word[-i]
        palindrome.append(letter)

    if ''.join(palindrome) == word:
        print('palindrome')

    else:
        print('not a palindrome')

def other_method(word=str):
    palindrome = word[::-1] #start:stop:step same as for loops
    print(palindrome)

if __name__ == '__main__':
    #main()
    other_method(input('Enter the word: '))