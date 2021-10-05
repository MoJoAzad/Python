class BankAccount:
    bank_name="Bank of America"
    all_accounts=[]

    def __init__(self, int_rate, balance=1000): 
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance+=amount
        return self
        
    def withdraw(self, amount):
        self.balance-=amount
        return self

    def display_account_info(self):
        print(f"BankAccount:{self.int_rate}Balance:{self.balance}")
        return self
    
    def yield_interest(self):
        self.balance+=self.balance*0.01
        return self

BankAccount('Bank of America')
Bank_of_America=BankAccount('Bank of America ')
Chase=BankAccount('Chase Bank ')

Bank_of_America.deposit(100).deposit(200).deposit(15).withdraw(50).yield_interest().display_account_info()

Chase.deposit(300).deposit(500).withdraw(100).withdraw(100).withdraw(55).yield_interest().display_account_info()
