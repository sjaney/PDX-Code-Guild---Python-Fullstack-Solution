# Lab 8v1 Guess the Number

import random

computer = random.randint(1, 10)

print("Let's play guess the number!")

user = input('Please guess a number between 0-10: ')
user = int(user) 

attempts = 0

while attempts < 9:
    attempts = attempts + 1

    if computer == user:
        print(f'You guessed correct! Took you {attempts} guesses!')
        break

    else:
        user = int(input('Try again: '))

if attempts == 9:
    print('You ran out of tries. Better luck next time.')








        



