class BankAccount:
    def __init__(self,account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance


    def deposit(self,amount):
       if amount> 0:
           self.balance += amount
           print(f"${amount}has been deposited into the account.")

       else:
           print("Invalid deposit amount.Please enter a positive value.")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount}has been withdrawn from the account.")

        else:
            print("Invalid withdrawal amount.Please enter a valid value.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name:{self.owner_name}")
        print(f"Current Balance:${self.balance}")


#Creating instances of BankAccount class
account1= BankAccount("1234567890","Iremnur Kurt")
account2= BankAccount("0987654321","Einstein")

#Performing account operations
account1.display_balance()
account1.deposit(1000)
account1.withdraw(500)
account1.display_balance()

account2.display_balance()
account2.withdraw(1000)
account2.deposit(2000)
account2.display_balance()