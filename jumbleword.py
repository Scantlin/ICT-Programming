import random

def main():
    print('------------ This is to jumble the word ------------')
    try:
        #Dataset of the word
        data = ['encantadia', 'anaca', 'love', 'you', 'scant', 'orange']

        choices = int(input(f'enter a number between 0-{len(data) -1 }: ')) #entering the choices from the dataset

        word = data[choices].upper() #convert the word into uppercase so that it will be generalize

        convert = list(map(str, word)) #make the word listed as list to make it easy to randomized

        #shuffle it 3times
        for i in range(len(word)):
            random.shuffle(convert)
 
        jumbled_word = ''.join(convert) #after shuffle the list, make it into sting literal

        print(f'Jumbled word: {jumbled_word}')

        print(f'Information: \nnumber of word: {len(word)}') #make an information about the number

        guess = input('Enter your guess: ').upper().strip() #this will be the guess input for the user

        if len(guess) == len(word):
            #checking if the word is not match on the guess so that it will loop until the answer is correct
            Correct = (word != guess)

            while Correct:
                print('your wrong, try it again')
                guess = input('Enter your guess: ').upper().strip()
                Correct = (word != guess)
    
            print('YOU GOT IT RIGHT')

        else:
            print('you enter a word that is not much on the length of the jumbled word')

    except Exception as e:
        print(e)

    finally:
        print('------------ Thank you for playing it --------------')


if __name__ == '__main__':
    main()