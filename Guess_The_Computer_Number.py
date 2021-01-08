#Simple python game where player guesses a randomly generated number
#January 7 2020
#Anjali Bhardwaj
import random

#store the previous guesses in list
prev_guess = [0]

#Computer randomly generates number
com_num = random.randint(1, 100)

# initialize variables
count = 0
user_in = 0

# continue game as long as the user input is not the random number.
while user_in != com_num:

    #User input
    user_in = int(input(f'\nEnter a guess from 1 to 100: '))

    #check if user_input in within bounds
    if user_in < 1 or user_in > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    #Add guess to list
    prev_guess.append(user_in)

    #Update counter
    count += 1

    #when the first user input in entered it will go to the else statement since prev_guess[-2] == 0.
    #if 0 will always evaluate to false, and if non-zero numbers will evalute to true.

    if prev_guess[-2]:

        #Compare the difference between the random number and the user input to see if it is smaller than
        #the difference between the random number and the previous guess.

        if abs(com_num-user_in) < abs(com_num-prev_guess[-2]):
            print('Warmer!')
        else:
            print('Colder!')
    else:
        #For the first guess, tell the user if they are 10 digits near or far from the random number
            if abs(user_in-com_num) <= 10:
                print("Warm!")
            elif abs(user_in-com_num) >= 10:
                print("Cold!")

else:
    #once the user gets the correct guess, print a message and tell them their attempts
    print(f"Congrats you guessed it in {count} tries.".format())
