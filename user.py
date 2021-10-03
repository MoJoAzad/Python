class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account_balance=1000
    def make_deposit(self, amount):
        self.account_balance+=amount
    def make_withdrawl(self, amount):
        self.account_balance-=amount
    # def transfer_money(self, other_user,amount):
        

        User("Mohammed", "MoMo@email.com")
Mohammed=User("Mohammed", "MoMo@email.com")
David=User("David", "david@gamil.com")
Natasha=User("Natasha", "N@yahoo.com")

Mohammed.make_withdrawl(100)
Mohammed.make_deposit(200)
Mohammed.make_deposit(50)
Mohammed.make_deposit(45)

David.make_withdrawl(200)
David.make_withdrawl(200)
David.make_deposit(300)
David.make_deposit(15)

Natasha.make_deposit(500)
Natasha.make_withdrawl(200)
Natasha.make_withdrawl(5)
Natasha.make_withdrawl(150)

print(Mohammed.name, '$',Mohammed.account_balance)
print(David.name, '$', David.account_balance)
print(Natasha.name, '$', Natasha.account_balance)
