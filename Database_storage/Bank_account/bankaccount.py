
class BankAccount:
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("You deposited {} to {}".format(self.balance, self.name))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("You widthdrew {} to {}".format(self.balance, self.name))
        else:
            print("{} you do not have enough funds".format(self.name))
    def print_balance(self):
        return "You balance is {}".format(self.balance)


user1 = BankAccount('Chad')

user1.deposit(1000)