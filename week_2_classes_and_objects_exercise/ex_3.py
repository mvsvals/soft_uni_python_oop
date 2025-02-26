class Account:
    def __init__(self, _id: int, name: str, balance: int = 0):
        self.balance = balance
        self.name = name
        self.id = _id


    def credit(self, amount):
        self.balance += amount
        return self.balance


    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"


    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


