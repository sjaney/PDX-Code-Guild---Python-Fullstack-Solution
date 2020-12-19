# Lab 6v2 Password Generator


import random
import string

letters = string.ascii_letters
numbers = string.digits
special_characters = string.punctuation
random_pass = ''

password = input('Would you like to generate a password?: ').lower()

if password == 'no':
    print('Goodbye!')

if password == 'yes':
    ask = int(input('How long would you like the password to be?: '))
    while len(random_pass) <= ask:
        random1 = random.choice(letters + numbers + special_characters)
        random_pass += random1

print(random_pass)