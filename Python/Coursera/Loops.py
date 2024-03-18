# x = 0
# while x <5:
#     print("Not there yet! x = " + str(x))
#     x = x + 1
# print("Not there yet! x = " + str(x))

# program to generate a random number and 5 chances to guess it

import random
number = random.randint(1, 25)
number_of_guesses = 0
number_failed_type_range = 10
attempts = 5
guess = int()

while number_of_guesses < 5:
    print('Guess a number between 1 and 25: ')
    while True:
        guess = input() 
        guess=int(guess)
        if guess in range(1, 25):
                # print('Guess a number between 1 and 25: ')
                number_of_guesses += 1      #This is the same as a = a +1
                if guess == number:
                    break
                elif number_of_guesses == 5:
                    break
                else:
                    attempts = attempts -1
                    print("Nope! Try again. Attempts left = " + str(attempts))

        else:
            print("You MUST enter a value between 1 and 25. Please type a number again. You only have " + str(number_failed_type_range) + ' left.')
            number_failed_type_range -= 1

if guess == number:
    print("Correct! You guessed the number in " + str(number_of_guesses) + ' tries\n')
else:
    print("You did not guess the number. The number was " + str(number) + '.\n')


