from class_12_Assignment1 import BankAccount
# Part 2: Creating Specialized Accounts
# Interest Rewards Account (InterestRewardsAcct):

# Task: add below functionality
# 1, This account rewards users by adding a 5% bonus to any amount deposited.
class InterestRewardsAcct(BankAccount):
    def __init__(self, name, amount=0):
        super().__init__(name, amount)
        self.interest_rate = 0.05
    
    def deposit(self, amount):
        self.balance += amount + (self.interest_rate*amount)

if __name__ == '__main__':
    # PART 2
    # Every InterestRewardsAcct user always receive 5% reward on adding more money
    Jim = InterestRewardsAcct(1000, "Jim")

    Jim.get_balance()

    Jim.deposit(100) # it should add $100 + Reward amount of extra 5% i.e (%100 * 1.05)

    Jim.get_balance() # it should display $1105

    Dave = BankAccount(1000, "Dave")
    Jim.transfer(100, Dave) # should add $100 to Dave account and remove $100 from Jim's account

    Jim.get_balance() # it should display $1005.00