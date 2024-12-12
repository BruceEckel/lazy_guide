#: type_reassignment.py


n: int = 11
print(f"{type(n) = }")

n = "string"
# The IDE complains:
# Expected type 'int', got 'str' instead

print(f"{type(n) = }")
