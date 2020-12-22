# Lab 7 Rock Paper Scissors

import random

print("Let's play rock paper scissor!")

user = input('Choose one: rock, paper or scissors: ').lower()

computer = ['rock', 'paper', 'scissors']
random_answer = random.choice(computer)


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
