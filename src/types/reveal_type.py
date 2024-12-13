#: reveal_type.py
from typing import reveal_type

b: bool = True
print(f"{reveal_type(b) = }")

s = "a string"
print(f"{reveal_type(s) = }")
#| reveal_type(s) = 'a string'

n = None
print(f"{reveal_type(n) = }")
#| reveal_type(n) = None

n = 1.23
print(f"{reveal_type(n) = }")
#| reveal_type(n) = 1.23
