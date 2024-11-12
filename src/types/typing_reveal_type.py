#: typing_reveal_type.py
from typing import reveal_type

from validate_output import console

b: bool = True
print(f"{reveal_type(b) = }")
console == """
reveal_type(b) = True
"""
s = "a string"
print(f"{reveal_type(s) = }")
console == """
reveal_type(s) = 'a string'
"""
n = None
print(f"{reveal_type(n) = }")
console == """
reveal_type(n) = None
"""
n = 1.23
print(f"{reveal_type(n) = }")
console == """
reveal_type(n) = 1.23
"""
