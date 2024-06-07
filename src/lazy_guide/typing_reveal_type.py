from typing import reveal_type
b : bool = True
print(f"{reveal_type(b) = }")
# reveal_type(b) = <class 'bool'>
s = "a string"
print(f"{reveal_type(s) = }")
# reveal_type(s) = <class 'str'>
n = None
print(f"{reveal_type(n) = }")
# reveal_type(n) = <class 'NoneType'>
n = 1.23
print(f"{reveal_type(n) = }")
# reveal_type(n) = <class 'float'>