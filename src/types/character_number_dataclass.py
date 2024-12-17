# character_number_dataclass.py
from dataclasses import dataclass
from typing import Union


@dataclass
class CharNum:
    ch: str
    nn: int

    def __post_init__(self):
        if len(self.ch) != 1:
            raise ValueError("ch must be a 1-char str")
        if not (0 < self.nn < 10):
            raise ValueError("Required: 0 < nn < 10")


@dataclass
class Rslt:  # Result
    type_is: bool
    val: Union[CharNum, str]


def is_charnum(val: dict) -> Rslt:
    try:
        # Attempt to create a CharNum instance:
        return Rslt(True, CharNum(**val))
    except (TypeError, ValueError) as e:
        match e:
            case TypeError():
                return Rslt(False, f"TypeError: {val}")
            case ValueError() as e:
                return Rslt(False, f"ValueError: {val} {e.args[0]}")


print("\n".join([str(is_charnum(f)) for f in [
    {"ch": "a", "nn": 1},
    {"Letter": "b", "nn": 2},
    {"ch": 9, "nn": 3},
    {"ch": "d", "nn": "x"},
    {"ch": "ee", "nn": 5},
    {"ch": "f", "nn": 11},
]]))
## Rslt(type_is=True, val=CharNum(ch='a', nn=1))
## Rslt(type_is=False, val="TypeError: {'Letter':
## 'b', 'nn': 2}")
## Rslt(type_is=False, val="TypeError: {'ch': 9,
## 'nn': 3}")
## Rslt(type_is=False, val="TypeError: {'ch': 'd',
## 'nn': 'x'}")
## Rslt(type_is=False, val="ValueError: {'ch':
## 'ee', 'nn': 5} ch must be a 1-char str")
## Rslt(type_is=False, val="ValueError: {'ch':
## 'f', 'nn': 11} Required: 0 < nn < 10")
