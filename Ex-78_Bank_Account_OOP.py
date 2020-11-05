# Ex-78_Bank_Account_OOP.py

'''Bank Account OOP Exercise

Define a new class called BankAccout.

-Each BankAccount should have an owner, specified when a new BankAccount is
created like BankAccount("Charlie")
-Each BankAccount should have a "balance attribute  that always stars out as 0.0
'''

# Define Bank Account Below:

#Bank Account Exercise Solution:
#Here's my BankAccount class:

class BankAccount:
 
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
    def deposit(self, amount):
        self.balance += amount
        return self.balance

user1 = BankAccount("Joe")
print(user1.getBalance()) # 0.0
