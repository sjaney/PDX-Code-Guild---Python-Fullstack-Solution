# Lab 12 Blackjack Advice

cards = {
    'A': 1,
    'J': 10,
    'Q': 10,
    'K': 10
}


# Welcome message and giving user what to choose
print('Welcome to Blackjack Advice. \nChoose by selecting from the following: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K ')


# Picking cards
first_card = input('Pick your first card: ').upper()
second_card = input('Pick your second card: ').upper()
third_card = input('Pick your third card: ').upper()

# Giving face cards a value using dictionary
for value in cards:
    if first_card == value: 
        first_card = cards[value]
        break

for value in cards:
    if second_card == value: 
        second_card = cards[value]
        break

for value in cards:
    if third_card == value: 
        third_card = cards[value]
        break

# Adding total for 
total = int(first_card) + int(second_card) + int(third_card)


# Advice
if total == 21:
    print(f'{total} Blackjack!')
elif total < 17:
    print(f'{total} Hit')
elif total >= 17 and total < 21:
    print(f'{total} Stay')
elif total > 21:
    print(f'{total} Already Busted')