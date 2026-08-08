class BankAcc:
    count=8020261
    def __init__(self, acc_name, balance):
        self.acc_no = BankAcc.count
        BankAcc.count += 1
        self.acc_name = acc_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        return self.balance