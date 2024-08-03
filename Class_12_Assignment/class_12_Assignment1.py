# Part 1: Introduction to the Base Class
# Understanding BankAccount:

# Task: Create a base class called BankAccount with the following attributes and methods:

# Attributes:
# balance: The initial amount of money in the account.
# name: The name of the account.

# Methods:
# get_balance: Print the current balance.
# deposit: Add a specified amount to the balance.
# withdraw: Subtract a specified amount from the balance if sufficient funds are available.
# transfer: Transfer a specified amount to another account.

class BankAccount:
    def __init__(self, initial_balance,name):
        self.name = name
        self.balance = initial_balance
    
    def get_balance(self):
        print (self.balance)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into {self.name}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.name}. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")
    def transfer(self, amount, account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            account.balance += amount
            print(f"Transferred {amount} from {self.name} to {account.name}. New balances: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid transfer amount.")

if __name__ == "__main__":

    Dave = BankAccount(1000, "Dave")
    Sara = BankAccount(2000, "Sara")

    Dave.get_balance() # should display $1000
    Sara.get_balance() # should display $2000

    Sara.deposit(500) # add 500 in Sara's account
    Sara.get_balance() # should display $2500

    Dave.withdraw(10000) # it should raise an error saying "Sorry, account 'Dave' only has a balance of $1000"
    Dave.withdraw(10)   # should subtract $10 from Dave's account
    Dave.get_balance()  # should display $990

    Dave.transfer(10000, Sara) # it should raise an error saying "Sorry, account 'Dave' only has a balance of $990"
    Dave.transfer(100, Sara)   # should add $100 to Sara's account and remove $100 from Dave's account

    Dave.get_balance() # should display $890
    Sara.get_balance() # should display $2600