# Lab 11 Make Change

quarter = 0.0
dime = 0.0
nickel = 0.0
penny = 0.0

print('Welcome to the Change Maker 5000')

while True:

    amount = float(input('Please enter a dollar amount: '))

    if quarter < amount: 
        quarter = amount // .25
        amount = amount - (quarter * .25)
       
    if dime < amount:
        dime = amount // .10
        amount = amount - (dime * .10)
    
    if nickel < amount:
        nickel = amount // .05
        amount = amount - (nickel * .05)
        
    if penny < amount:
        penny = amount // .01
        amount = amount - (penny * .01)
        
    print(f"{int(quarter)} quarters, {int(dime)} dimes, {int(nickel)} nickels, {int(penny)} pennies")

    play_again = input('Would you like to play again? y/n: ').lower()

    valid_choices = ['yes', 'y', 'n', 'no']

    if play_again in valid_choices == 'no' or 'n':
        print('Have a good day!')
        break

    if play_again in valid_choices == 'yes' or 'y':
        print(input('Please enter a dollar amount: '))