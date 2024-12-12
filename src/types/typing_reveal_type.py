#: typing_reveal_type.py
from typing import reveal_type



b: bool = True
print(f"{reveal_type(b) = }")

s = "a string"
print(f"{reveal_type(s) = }")

n = None
print(f"{reveal_type(n) = }")

n = 1.23
print(f"{reveal_type(n) = }")
