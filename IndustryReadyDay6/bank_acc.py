class bank:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount} to {self.name}'s account. Current balance is {self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdrew {amount} from {self.name}'s account. Current balance is {self.balance}")
        else:
            print("Insufficient balance for withdrawal.")
acc=bank("ganga")
acc.deposit(5000)
acc.withdraw(3000)
acc.withdraw(20000)  # Attempting to withdraw more than the balance