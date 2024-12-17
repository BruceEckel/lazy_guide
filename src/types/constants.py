# constants.py
from typing import Final

# Traditional constant:
GOLDEN_RATIO = 1.61803
# Explicit type annotation:
pi: Final[float] = 3.14159

print(f"{type(pi) = }, {pi}")
## type(pi) = <class 'float'>, 3.14159
print(f"{type(GOLDEN_RATIO) = }, {GOLDEN_RATIO}")
## type(GOLDEN_RATIO) = <class 'float'>, 1.61803

pi = 4.0
# Produces:
# 'pi' is 'Final' and could not be reassigned:

GOLDEN_RATIO = 2.0
# Doesn't necessarily produce a warning
