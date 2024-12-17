# disallow_illegal_states.py
from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    amount: float

    def __post_init__(self):
        assert self.amount >= 0

    def __iadd__(self, other: "Money") -> "Money":
        return Money(self.amount + other.amount)

    def __isub__(self, other: "Money") -> "Money":
        return Money(self.amount - other.amount)


@dataclass
class Account:
    balance: Money
    
    def __post_init__(self):
        print(self)

    def deposit(self, money: Money) -> None:
        self.balance += money
        print(self)

    def withdraw(self, money: Money) -> None:
        self.balance -= money
        print(self)


account = Account(Money(50.0))
## Account(balance=Money(amount=50.0))
account.deposit(Money(100.0))
## Account(balance=Money(amount=150.0))
account.withdraw(Money(30.0))
## Account(balance=Money(amount=120.0))

try:
    account.deposit(Money(-10.0))
except AssertionError:
    print("failed: deposit(Money(-10.0))")
## failed: deposit(Money(-10.0))

try:
    account.withdraw(Money(150.0))
except AssertionError:
    print("failed: withdraw(Money(150.0))")
## failed: withdraw(Money(150.0))
