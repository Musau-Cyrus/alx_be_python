class BankAcount:
    def __init__(self):
        self.acount_balance = 0 

    def deposit(self, amount):
        self.acount_balance += amount

    def withdraw(self, amount):
        if self.acount_balance > 0:
            self.acount_balance -+ amount
            return True
        else:
            return False
        
    def display_balance():
        print('Current balance is: {self.acount_balance}')