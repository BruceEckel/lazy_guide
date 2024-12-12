#: letter_number_dataclass.py
import sys
from dataclasses import asdict, dataclass

if sys.version_info > (3, 13):  # TypeIs is available in Python 3.13+
    from typing import TypeIs
else:
    from typing_extensions import TypeIs

@dataclass
class LetterNumber:
    letter: str
    number: int

    def __post_init__(self):
        if len(self.letter) != 1:
            raise ValueError("letter must be a single character string")
        if not (0 < self.number < 10):
            raise ValueError("number must be an integer between 1 and 9")


def is_letter_number(val: dict) -> TypeIs[LetterNumber]:
    print(f"is_letter_number({val}): ", end="")
    try:
        # Attempt to create a LetterNumber instance:
        LetterNumber(**val)
    except (TypeError, ValueError):
        return False
    return True


letter_number_list: list[dict] = [
    {"letter": "a", "number": 1},
    {"Letter": "b", "number": 2},
    {"letter": 9, "number": 3},
    {"letter": "d", "number": "x"},
    {"letter": "ee", "number": 5},
    {"letter": "f", "number": 11},
    asdict(LetterNumber("g", 9)),
]

if __name__ == "__main__":
    [print(is_letter_number(f)) for f in letter_number_list]
