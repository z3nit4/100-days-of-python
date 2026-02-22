class BankAccount:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print(f"Deposit of {amount} successful. Your balance is: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal of {} successful. Final balance is: {}.".format(amount, self.balance))
        else:
            print("Insufficient funds")
    
    def display_balance(self):
        print(self.owner, self.balance)



# ===== Testing Section =====

account1 = BankAccount("Zeen", 500)

account1.display_balance()

account1.deposit(200)

account1.withdraw(100)

account1.withdraw(1000)  # Test insufficient funds

account1.display_balance()
