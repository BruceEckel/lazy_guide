# type_awareness.py


x = True
print(f"{type(x) = }")
## type(x) = <class 'bool'>

x = "a string"
print(f"{type(x) = }")
## type(x) = <class 'str'>

x = None
print(f"{type(x) = }")
## type(x) = <class 'NoneType'>

x = 11
print(f"{type(x) = }")
## type(x) = <class 'int'>

x = 1.23
print(f"{type(x) = }")
## type(x) = <class 'float'>

x = {"a", "b", "c"}
print(f"{type(x) = }")
## type(x) = <class 'set'>
