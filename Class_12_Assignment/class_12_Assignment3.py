from class_12_Assignment1 import BankAccount

# Part 3: Creating Specialized Accounts
# Savings Account (SavingsAcct):

# Task: add below functionality
# 1. This account rewards users by adding a 5% bonus to any amount deposited.
# 2. This account charges a $5 fee for every withdrawal.
# Ref: https://www.youtube.com/watch?v=PMFd95RgIwE

class SavingsAcct(BankAccount):
    def __init__(self, name, amount=0):
        super().__init__(name, amount)
        self.interest_rate = 0.05
        self.fee = 5
    
    def deposit(self, amount):
        if amount >0 :
            self.balance += amount + (self.interest_rate*amount)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance - self.fee:
            self.balance -= amount
            self.balance -= self.fee
            print(f"Withdrew {amount} from {self.name}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    def transfer(self, amount, account):
        if amount > 0 and amount <= self.balance - self.fee:
            self.balance -= amount
            self.balance -= self.fee
            account.balance += amount
            print(f"Transferred {amount} from {self.name} to {account.name}. New balance: {self.balance} ")
        else:
            print("Invalid transfer amount or insufficient funds.")

if __name__ == "__main__":
    # PART 3
    # Every SavingsAcct user always receive 5% reward on adding more money
    # Every SavingsAcct user always get panelty of $5 on reducing the money
    Blaze = SavingsAcct(1000, "Blaze")

    Blaze.get_balance() # it should display $1000

    Blaze.deposit(100)   # it should add $100 + Reward amount of extra 5% i.e (%100 * 1.05)
    Blaze.get_balance()  # should display $1105 (instead of 1100)

    Blaze.withdraw(10)   # should subtract $15 (instead of $10) from Blaze's account
    Blaze.get_balance()  # should display $1090 (instead of 1095)

    Sara = BankAccount(1000,"sara")
    Blaze.transfer(10000, Sara) # it should raise an error saying "Sorry, account 'Blaze' only has a balance of $1090"
    Blaze.transfer(1000, Sara) # it should add $1000 to Sara's account and subtract $1005 from Blaze account (instead of $1000)
    Blaze.get_balance()  # should display $85