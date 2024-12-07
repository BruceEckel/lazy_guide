#: disallow_illegal_states.py
# from validate_output import console
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

    def deposit(self, money: Money) -> None:
        self.balance += money

    def withdraw(self, money: Money) -> None:
        self.balance -= money


account = Account(Money(50.0))
print(account)
account.deposit(Money(100.0))
print(account)
account.withdraw(Money(30.0))
print(account)

try:
    account.deposit(Money(-10.0))
except:
    print("failed: deposit(Money(-10.0))")

try:
    account.withdraw(Money(150.0))
except:
    print("failed: withdraw(Money(150.0))")
