# type_reassignment.py


n: int = 11
print(f"{type(n) = }")
## type(n) = <class 'int'>

n = "string"
# The IDE complains:
# Expected type 'int', got 'str' instead

print(f"{type(n) = }")
## type(n) = <class 'str'>
