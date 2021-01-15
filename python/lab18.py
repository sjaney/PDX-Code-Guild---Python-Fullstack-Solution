# Lab 18 - ATM

class ATM:
    def __init__(self, balance = 0, apr = 0.001):
        self.balance = balance
        self.apr = apr
        self.transactions = []

    # balance() returns the account balance
    def check_balance(self):
        return self.balance

    # deposit(amount) deposits the given amount in the account
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}') # add to list of transactions

    # check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        # return self.balance >= amount
        self.balance -= amount
        if self.balance >= 0:
            return True
        else:
            return False
        
    # withdraw(amount) withdraws the amount from the account and returns it
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'User withdrew ${amount}') # add to list of transactions

    # calc_interest() returns the amount of interest calculated on the account
    def calc_interest(self):
        return self.balance * self.apr

    
atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ').lower()
    if command == 'balance':
        balance = atm.check_balance() # call the balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw? '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')   
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'print transaction':
        print (', '.join(atm.transactions)) # print transactions
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('print transaction - transaction history')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
