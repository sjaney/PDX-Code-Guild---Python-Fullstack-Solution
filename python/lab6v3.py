# Lab 6v3 Password Generator

import random
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
special_characters = string.punctuation
random_upper = ''
random_lower = ''
random_number = ''
random_characters = ''

password = input('Would you like to generate a password?: ').lower()

if password == 'no':
    print('Goodbye!')

if password == 'yes':
    uppercase_letters = int(input('How many uppercase letters would you like?: '))
    while len(random_upper) < uppercase_letters:
        random1 = random.choice(uppercase)
        random_upper += random1

    lowercase_letters = int(input('How many lowercase letters would you like?: '))
    while len(random_lower) < lowercase_letters:
        random2 = random.choice(lowercase)
        random_lower += random2

    num_of_num = int(input('How many numbers would you like?: '))
    while len(random_number) < num_of_num:
        random3 = random.choice(numbers)
        random_number += random3

    num_of_charaters = int(input('How many special characters would you like?: '))
    while len(random_characters) < num_of_charaters:
        random4 = random.choice(special_characters)
        random_characters += random4

    random_pass = list(random_upper + random_lower + random_number + random_characters)
    random.shuffle(random_pass)

print(''.join(random_pass))

