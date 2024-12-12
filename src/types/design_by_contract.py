#: design_by_contract.py
from typing import Final


def invariant(balance: float) -> float:
    assert balance >= 0
    return balance


def deposit(balance: float, amount: float) -> float:
    invariant(balance)
    # Precondition
    assert amount > 0
    old_balance: Final[float] = balance
    new_balance: Final[float] = old_balance + amount
    # Postcondition
    assert new_balance > old_balance
    return invariant(new_balance)


def withdraw(balance: float, amount: float) -> float:
    invariant(balance)
    # Preconditions
    assert balance >= amount
    assert amount > 0
    old_balance: Final[float] = balance
    new_balance: Final[float] = old_balance - amount
    # Postcondition
    assert new_balance < old_balance
    return invariant(new_balance)


print(balance := deposit(100.0, 50.0))
#| 150.0)
print(withdraw(balance, 30.0))
#| 120.0)
