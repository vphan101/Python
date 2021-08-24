class User:		# declare a class and give it name User
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

guido = User()
monty = User()

print(guido.name)	# output: Michaelcopy
print(monty.name)	# output: Michael

guido.name = "Guido"
monty.name = "Monty"

print(guido.name)	#output: Guido
print(monty.name)	#outpur: Monty

class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount):
        self.account_balance -=amount

    def display_user_balance(self):
        print("User:", self.name, "--------------- ","Balance:$", self.account_balance)

Vinh = User("Vinh Phan", "Vinh@email.com")
Monty = User("Monty Python", "monty@python.com")
print(Vinh.name)	# output: Guido van Rossum
print(Monty.name)	# output: Monty Python

Vinh.make_deposit(100)
Vinh.make_deposit(200)
Vinh.make_deposit(300)
print(Vinh.account_balance)

Vinh.make_withdrawal(1)
print(Vinh.account_balance)

Vinh.display_user_balance()

Monty.make_deposit(5)
Monty.make_deposit(100)
Monty.make_withdrawal(10)
Monty.make_withdrawal(4)
print(Monty.account_balance)
Monty.display_user_balance()

        
    


