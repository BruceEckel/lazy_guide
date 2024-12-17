# typed_dict.py
import sys
from typing import TypedDict

if sys.version_info > (3, 13):  # TypeIs is available in Python 3.13+
    from typing import TypeIs
else:
    from typing_extensions import TypeIs


class LetterNumber(TypedDict):
    letter: str
    number: int


letter_number_list: list[LetterNumber] = [
    {"ch": "a", "nn": 1},
    {"Letter": "b", "nn": 2},
    {"ch": 9, "nn": 3},
    {"ch": "d", "nn": "x"},
    {"ch": "ee", "nn": 5},
    {"ch": "f", "nn": 11},
    LetterNumber(letter="g", number=9),
]


def is_letter_number(val: dict) -> TypeIs[LetterNumber]:
    print(f"is_letter_number({val}): ", end="")
    try:
        # Attempt to access values with Foo keys:
        letter, number = val["ch"], val["nn"]
    except KeyError:
        return False
    if not isinstance(letter, str):
        return False
    if not isinstance(number, int):
        return False
    return len(letter) == 1 and 0 < number < 10


if __name__ == "__main__":
    [print(is_letter_number(f)) for f in letter_number_list]
## is_letter_number({'ch': 'a', 'nn': 1}): True
## is_letter_number({'Letter': 'b', 'nn': 2}):
## False
## is_letter_number({'ch': 9, 'nn': 3}): False
## is_letter_number({'ch': 'd', 'nn': 'x'}): False
## is_letter_number({'ch': 'ee', 'nn': 5}): False
## is_letter_number({'ch': 'f', 'nn': 11}): False
## is_letter_number({'letter': 'g', 'number': 9}):
## False
