#: type_reassignment.py
from validate_output import console

n: int = 11
print(f"{type(n) = }")
console == """
type(n) = <class 'int'>
"""

n = "string"
# The IDE complains:
# Expected type 'int', got 'str' instead

print(f"{type(n) = }")
console == """
type(n) = <class 'str'>
"""
