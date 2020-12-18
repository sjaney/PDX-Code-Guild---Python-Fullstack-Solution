# Lab 4 - Magic Eight Ball

import random

while True:
    user = input('Hello! Welcome to the magic eight ball. \nAsk me anything or enter "done" to quit: ').lower()
    if user == 'done':
        print('Goodbye!')
        break

    predictions = ['It is certain', 'Without a doubt', 'Cannot predict now', 'Very doubtful']
    answer = random.choice(predictions)

    print(answer)