#: typed_dict.py
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
    {"letter": "a", "number": 1},
    {"Letter": "b", "number": 2},
    {"letter": 9, "number": 3},
    {"letter": "d", "number": "x"},
    {"letter": "ee", "number": 5},
    {"letter": "f", "number": 11},
    LetterNumber(letter="g", number=9),
]


def is_letter_number(val: dict) -> TypeIs[LetterNumber]:
    print(f"is_letter_number({val}): ", end="")
    try:
        # Attempt to access values with Foo keys:
        letter, number = val["letter"], val["number"]
    except KeyError:
        return False
    if not isinstance(letter, str):
        return False
    if not isinstance(number, int):
        return False
    return len(letter) == 1 and 0 < number < 10


if __name__ == "__main__":
    [print(is_letter_number(f)) for f in letter_number_list]
