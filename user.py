class User:
    def __init__(self, name):
        self.name=name
        self.amount=1000

    def make_deposit(self, amount):
        self.amount+=amount
        return self

    def make_withdrawl(self, amount):
        self.amount-=amount
        return self

    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.amount}")

User('Mohammed')
Mohammed=User("Mohammed")
David=User("David")
Natasha=User("Natasha")

Mohammed.make_withdrawl(100).make_deposit(200).make_deposit(50).make_deposit(45).display_user_balance()

David.make_withdrawl(200).make_withdrawl(200).make_deposit(300).make_deposit(15).display_user_balance()

Natasha.make_deposit(500).make_withdrawl(200).make_withdrawl(5).make_withdrawl(150).display_user_balance()


