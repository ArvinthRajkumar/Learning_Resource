from dataclasses import dataclass, field

class InsufficientFunds(Exception): pass

@dataclass
class Account:
    owner: str
    balance: int = 0
    history: list = field(default_factory=list)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds(f"balance {self.balance}, requested {amount}")
        self.balance -= amount
        self.history.append(("withdraw", amount))

a = Account("Ada")
a.deposit(100); a.withdraw(30)
try:
    a.withdraw(500)
except InsufficientFunds as e:
    print("error:", e)
print(a.balance, a.history)
