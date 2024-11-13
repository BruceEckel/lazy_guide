#: type_awareness.py
from validate_output import console

x = True
print(f"{type(x) = }")
console == """
type(x) = <class 'bool'>
"""

x = "a string"
print(f"{type(x) = }")
console == """
type(x) = <class 'str'>
"""

x = None
print(f"{type(x) = }")
console == """
type(x) = <class 'NoneType'>
"""

x = 1.23
print(f"{type(x) = }")
console == """
type(x) = <class 'float'>
"""

x = 11
print(f"{type(x) = }")
console == """
type(x) = <class 'int'>
"""

x = {"a", "b", "c"}
print(f"{type(x) = }")
console == """
type(x) = <class 'set'>
"""
