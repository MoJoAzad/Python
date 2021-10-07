from Bank_account import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line

# class User:
#     def example_method(self):
#     	# we can call the BankAccount instance's methods
#         self.account.deposit(100)
#     	# or access its attributes
#     	print(self.account.balance)

Mo=User('Mo', 'mo@gmail.com')
Mo.account.deposit(1200).withdrawl(500).display_account_info()

