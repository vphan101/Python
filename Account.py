class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = .01
        self.balance = 0

    def deposit(self, amount):
        self.balance +=amount
        return self
        
        
    def withdraw(self, amount):
        self.balance -= amount
        
        print("$",self.balance)

        if self.balance <0:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print("banker: $", self.balance)
        
        

    def yield_interest(self):
        self.balance * self.int_rate


Account1 = BankAccount(.01, 0)
Account2 = BankAccount(.01, 0)


Account1.deposit(25).deposit(25).withdraw(10).withdraw(5).withdraw(5)
print(Account1.display_account_info())


Account2.deposit(5).deposit(40).deposit(5).withdraw(100)
print(Account2.display_account_info())











