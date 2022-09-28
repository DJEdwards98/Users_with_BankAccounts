from BankAccount import BankAccount


class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(.4,400)
        
    def make_deposit(self,amount):
        self.account.deposit(amount)


    def make_withdrawl(self,amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        self.account.display_account_info()


