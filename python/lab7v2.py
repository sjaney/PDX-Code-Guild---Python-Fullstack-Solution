# Lab 7v2 Rock, Paper, Scissors

import random

print("Let's play rock paper scissor!")


while True: 

    user = input('Choose the following: rock, paper, scissors or "done" to quit: ').lower()

    computer = ['rock', 'paper', 'scissors']
    random_answer = random.choice(computer)
    valid_choices = 'rock', 'paper', 'scissors', 'done'
    

    while user not in valid_choices:
        user = input('Invalid selection. Please try again: ').lower()

    if user == 'done':
        print ('Goodbye!')
        break 

    if user == random_answer:
        message = f"Your {user} ties computer's {random_answer}"

    elif user == 'paper' and random_answer == 'rock':
        message = f"Your {user} beats computer's {random_answer}"

    elif user == 'paper' and random_answer == 'scissors':
        message = f"Your {user} lost to computer's {random_answer}"

    elif user == 'rock' and random_answer == 'paper':
        message = f"Your {user} lost to computer's {random_answer}"

    elif user == 'rock' and random_answer == 'scissors':
        message = f"Your {user} beats computer's {random_answer}"

    elif user == 'scissors' and random_answer == 'rock':
        message = f"Your {user} lost to computer's {random_answer}"

    elif user == 'scissors' and random_answer == 'paper':
        message = f"Your {user} beats computer's {random_answer}"


    print(message)