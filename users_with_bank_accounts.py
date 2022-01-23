from tkinter import N


class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance=amount
        return self

    def withdrawl(self, amount):
        if (self.balance-amount) >=0:
            self.balance-=amount
        else:
            print(f"Insuficient Funds: Chanrge a $5 fee")
            self.balance-=5
        return self
    
    def display_account_info(self):
        print(f"Balance:{self.balance}")
        return self

    def yield_interest(self):
        if self.balance >0:
            self.balance+=(self.balance*self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for accounts in cls.accounts:
            accounts.display_account_info()

class User:
    def __init__(self, name):
        self.name=name
        self.account={
            'checking': BankAccount(.02,1000),
            'savings': BankAccount(.01, 5000)
        }

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

mohammed = User("Mohammed")

mohammed.account['checking'].deposit(1000).yield_interest()
mohammed.account['savings'].deposit(550).yield_interest()
mohammed.display_user_balance()
