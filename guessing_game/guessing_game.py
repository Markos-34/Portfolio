#package
import random

#To be able to get in the while loop
play_again = 'y'

#if user enter y the games continues, n otherwise
while play_again != 'n':
    #variables
    computer_number = random.randint(1, 100)
    user_guess = 0
    count = 0

    while int(user_guess) != computer_number:
        user_guess = input("Please gues a number: ")
        #compare the user guess with the computer number 
        if int(user_guess) < computer_number:
            print("\nYou guess too low!!")
            count += 1
        #compare the user guess with the computer number     
        elif int(user_guess) > computer_number:
            print("\nYou guess too high!")
            count += 1
    #End of while
            
    print("\nCongratulation!! You find it!!")
    print("\nYou take " + str(count) + "guesses!")
    play_again = input("\nDo you want to play again y/n?")
    #Ask user to continue the game or not
    if play_again == 'y':
        print("\nGreat! Let's play again!")
        play_again = 'y'
                
    else:
        play_again = 'n'
        print("\nBye!!")