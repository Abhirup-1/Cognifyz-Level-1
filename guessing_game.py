# This is a guessing game ( of numbers and alphabets )

import random
import string

#------------------------------------------------NUMBER GAME------------------------------------------------
def number_game():
    def guess_number_rules():
        print('\n------------GAME RULES------------')
        print('1. You have to enter an integer number only.')
        print('2. You have to enter the range in which you are guessing a number.')
        print('3. The number should be within the range provided.')
        print('\nNOTE -> THE GREATER THE RANGE , THE GREATER THE CHANCE OF YOUR LOSS.\n')

    def guess_number(start_pos , end_pos , user_guess):
        computer_guess = random.randint(start_pos , end_pos)
            
        if(computer_guess == user_guess):
            print('---------------------------')
            print('Yayy ! You win.')
            print('---------------------------')
        else:
            print('---------------------------')
            print('You lose :( !')
            print('---------------------------')

    guess_number_rules()

    while True:
        start_pos = int(input('\nEnter starting position: '))
        end_pos = int(input('Enter ending position: '))

        user_guess = int(input('Enter the number you are guessing : '))

        guess_number(start_pos , end_pos , user_guess)

        print('Do you want to continue playing?')
        choice = int(input('press 1 for yes and 0 for no : '))
        if(choice==1):
            continue
        else: 
            break
#------------------------------------------------ALPHABET GAME------------------------------------------------
def alphabet_game():
    def guess_alphabet_rules():
        print('\n------------GAME RULES------------')
        print('1. You have to enter an alphabet only.')
        print('2. The alphabet should be in lowercase. ')
        print('\nNOTE -> THE GREATER THE RANGE , THE GREATER THE CHANCE OF YOUR LOSS.\n')



    def guess_alphabet(start_alphabet,end_alphabet,user_guess):
        start_pos = string.ascii_lowercase.index(start_alphabet)
        end_pos = string.ascii_lowercase.index(end_alphabet)

        computer_guess = random.randint(start_pos,end_pos)

        return string.ascii_lowercase[computer_guess]
            

    guess_alphabet_rules()

    while True:
        start_alphabet = input('\nEnter the starting alphabet: ')
        end_alphabet = input('\nEnter the ending alphabet: ')
        user_guess = input('\nEnter the alphabet you are guessing : ')

        result = guess_alphabet(start_alphabet,end_alphabet,user_guess)

        if(result == user_guess):
            print('---------------------------')
            print('Yayy ! You win.')
            print('---------------------------')
        else:
            print('---------------------------')
            print('You lose :( !')
            print('---------------------------')

        print('Do you want to continue playing?')
        choice = int(input('press 1 for yes and 0 for no : '))
        if(choice==1):
            continue
        else: 
            break

#------------------------------------------GAME CHOICE------------------------------------------
while True:
    print('Which guessing game you want to play?')
    print('Press 1 to play guessing number game.')
    print('Press 2 to play guessing alphabet game.')
    game_choice = int(input('Enter choice: '))
    if(game_choice==1):
        number_game()
    elif(game_choice == 2):
        alphabet_game()
    else:
        print('wrong choice !')
    
    print('\nDo you want to play another game ?')
    choice = int(input('press 1 for yes and 0 for no : '))
    if(choice==1):
        continue
    else: 
        break
