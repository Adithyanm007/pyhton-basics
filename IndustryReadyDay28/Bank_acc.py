class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if 0<amount<self.__balance:
            self.__balance-=amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    def get_balance(self):
        return self.__balance
bank=BankAccount("John Doe", 1000)
bank.deposit(500)
bank.withdraw(200)
print(f"Balance in acc of {bank.owner} is {bank.get_balance()}")
#print(bank.__balance)  # This will raise an AttributeError since __balance is private