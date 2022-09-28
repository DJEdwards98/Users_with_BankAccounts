from user import User
from BankAccount import BankAccount
dijon = User("Dijon","dijonedwards3@gmail.com")
print(dijon.name)

dijon.make_deposit(100)

dijon.display_user_balance()

dijon.make_withdrawl(20)

dijon.display_user_balance()
