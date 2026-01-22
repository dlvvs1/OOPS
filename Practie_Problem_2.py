'''Create Account class with 2 attributes - balance and account_number.
   Create methods for credit,debit and display_balance.'''

class  Account: # class definition
    def __init__(self, bal , acc_no): # constructor method
        self.balance = bal
        self.account_number = acc_no

    # credit method
    def credit(self , amount):
        self.balance += amount
        print(f"credited amount: {amount}. New balance: {self.balance}")

    #debit method
    def debit(self , amount):
        self.balance -= amount
        print(f"debited amount: {amount}. New balance: {self.balance}")

    #display_balance method
    def display_balance(self):
        print(f"Current balance: {self.balance}")


acc1 = Account(100000 , "ACC12345") # object of Account class
print(f"Account Number: {acc1.account_number}")
print(f"Initial Balance: {acc1.balance}")
acc1.credit(5000)
acc1.debit(2000)
acc1.display_balance()