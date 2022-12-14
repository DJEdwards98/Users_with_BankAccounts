class BankAccount:
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        
    
    def deposit(self, amount):
        self.balance= self.balance + amount
    
    def withdraw(self, amount):
        
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance = self.balance - amount
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        
    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate
        
