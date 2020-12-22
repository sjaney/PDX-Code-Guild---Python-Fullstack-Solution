# Lab 8v2 Guess the number


import random

print("Let's play guess the number!")
attempts = 0

while True:
    computer = random.randint(1, 10)

    user = input('Please guess a number between 0-10: ')

    while not user.isdigit():
        print("Invalid input. Enter again: ")
        user = input()

    user = int(user)

    attempts = attempts + 1

    if computer == user:
        print(f'You guessed correct! Took you {attempts} guesses.')
        break

    if user > computer or user < computer:
        print('Try again!')
  
