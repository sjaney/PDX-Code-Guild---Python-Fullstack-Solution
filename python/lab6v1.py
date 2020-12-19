# Lab 6v1 Password Generator

import random
import string

letters = string.ascii_letters
numbers = string.digits
special_characters = string.punctuation
random_pass = ''

password = input('Would you like to generate a password?: ').lower()

if password == 'no':
    print('Goodbye')
 
if password == 'yes':
    while len(random_pass) < 8:
        random1 = random.choice(letters + numbers + special_characters )
        random_pass += random1
        
print(random_pass)