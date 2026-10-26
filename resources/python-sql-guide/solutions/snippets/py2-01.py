class Account:
    bank = "PyBank"                       # class attribute, shared by all instances

    def __init__(self, owner, balance=0): # initialiser, runs on creation
        self.owner = owner                # instance attributes
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount
        return self.balance

    def __repr__(self):
        return f"Account({self.owner!r}, {self.balance})"

a = Account("Ada", 100)
a.deposit(50)
print(a, a.bank, Account.bank, a.balance)
b = Account("Ben")
print(b, a is b)
