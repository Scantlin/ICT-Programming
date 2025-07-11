import random
from datetime import datetime
import pytz

def main():
    print('------------ This is to jumble the word ------------')
    try:
        timezone = pytz.timezone('Asia/Manila')
        time = datetime.now(timezone).strftime('%H:%M')

        #Dataset of the word
        print(f'Start: {time}')
        data = ['encantadia', 'anaca', 'love', 'you', 'scant', 'orange', 'dog', 'Collo', 'Nathan']
        choices = int(input(f'enter a number between 0-{len(data) -1 }: ')) #entering the choices from the dataset
        word = data[choices].upper() #convert the word into uppercase so that it will be generalize
        lives = 3 #lives of the user
        convert = list(map(str, word)) #make the word listed as list to make it easy to randomized
        word_list = list(map(str, word)) #additional for checking to make sure the convert is well shuffled

        #shuffle it
        for i in range(len(word)):
            random.shuffle(convert)

            if convert != word_list: #additional conditions to avoid the convert return the shuffle, to make sure it is really shuffled
                break #exit the loop
            
 
        jumbled_word = ''.join(convert) #after shuffle the list, make it into sting literal

        print(f'Jumbled word: {jumbled_word}')
        print(f'Information: \nnumber of word: {len(word)}') #make an information about the number
        print('lives: 3')

        guess = input('Enter your guess: ').upper().strip() #this will be the guess input for the user

        if word == guess:
            print('you got it right')

        #checking if the word is not match on the guess so that it will loop until the answer is correct
        Correct_not = (word != guess)

        while Correct_not:
            lives -= 1
            print(f'lives: {lives}')

            not_in_word = [] #the storage of wrong character and sort it

            for i in range(len(guess)): #looping to see if the guessed input has wrong character
                if guess[i] not in word:
                    not_in_word.append(guess[i])

            if not_in_word == []:
                pass #nothing will be printed if there is no incorrect character
            else:
                print('wrong character:' , ', '.join(not_in_word))


            if lives == 0:
                    print('you lost')
                    break

            if len(guess) == len(jumbled_word):
                print('your wrong, try it again')
                guess = input('Enter your guess: ').upper().strip() #strip function is to make the space remove in the input, just in case    
            else:
                print('you enter a word that is not much on the length of the jumbled word')
                guess = input('Enter your guess: ').upper().strip()

            if guess == word:
                print('YOU GOT IT RIGHT')
                break

            Correct_not = (word != guess)

    except Exception as e:
        print(e)

    finally:
        print('------------ Thank you for playing it --------------')


if __name__ == '__main__':
    main()