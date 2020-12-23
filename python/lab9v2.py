# Lab 9v2 ROT Cipher

import string

print('Encrypt your word into a ROT Cipher.')

user = input('Enter a word(s) you would like to encrypt: ')

move = int(input('Enter an amount for rotation: '))

alphabet = string.ascii_lowercase
encryption = ''

for char in user:
    if char in alphabet:
        new_encrypt = alphabet.index(char) + move
        encryption += alphabet[new_encrypt % 26]

print(encryption)