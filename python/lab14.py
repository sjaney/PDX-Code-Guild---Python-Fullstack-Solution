# Lab 14 Number to Phrase

print('Number to Phrase Converter')

ones_digit = {
    0: 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10: 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    14 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    16 : 'eighteen',
    19 : 'nineteen'
}


tens_digit = {
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
}

tens_unit = {
    2 : 'twenty',
    3 : 'thirty',
    4 : 'forty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'ninety'
}

hundreds_digit = {
    100 : 'one hundred',
    200 : 'two hundred',
    300 : 'three hundred',
    400 : 'four hundred',
    500 : 'five hundred',
    600 : 'six hundred',
    700 : 'seven hundred',
    800 : 'eight hundred',
    900 : 'nine hundred',
    1 : 'one hundred',
    2 : 'two hundred',
    3 : 'three hundred',
    4 : 'four hundred',
    5 : 'five hundred',
    6 : 'six hundred',
    7 : 'seven hundred',
    8 : 'eight hundred',
    9 : 'nine hundred'
}


# Version 1
'''
user = int(input("Enter the digit you would like to convert: "))


if user < 20:
    print(ones_digit[user].capitalize())
elif user <= 99:
    if user in tens_digit:
        print(tens_digit[user])
    else:
        tens = tens_digit[user // 10]
        ones = ones_digit[user % 10]
        print(tens.capitalize() + ' ' + ones.capitalize())
'''


# Version 2
user = int(input("Enter the digit you would like to convert: "))


if user < 20:
    print(ones_digit[user].capitalize())
elif user <= 99:
    if user in tens_digit:
        print(tens_digit[user])
    else:
        tens = tens_unit[user // 10]
        ones = ones_digit[user % 10]
        print(tens.capitalize() + ' ' + ones.capitalize())
elif user <= 999:
    if user in hundreds_digit:
        print(hundreds_digit[user].title())
    else:
        hundreds = hundreds_digit[user // 100]
        number = user // 100
        user = user - (number * 100)
        tens = tens_unit[user // 10]
        ones = ones_digit[user % 10]
        print(hundreds.title() + ' ' + tens.capitalize() + ' ' + ones.capitalize())



