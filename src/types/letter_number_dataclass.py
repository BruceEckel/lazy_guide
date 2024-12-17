# letter_number_dataclass.py
import sys
from dataclasses import asdict, dataclass

if sys.version_info > (3, 13):  # TypeIs is available in Python 3.13+
    from typing import TypeIs, Union
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


@dataclass
class ILN_Result:
    type_is: TypeIs[LetterNumber]
    val: Union[LetterNumber, TypeError, ValueError]


def is_letter_number(val: dict) -> ILN_Result:
    try:  # Attempt to create a LetterNumber instance:
        return ILN_Result(True, LetterNumber(**val))
    except (TypeError, ValueError) as e:
        return ILN_Result(False, e)


letter_number_list: list[dict] = [
    {"letter": "a", "number": 1},
    {"Letter": "b", "number": 2},
    {"letter": 9, "number": 3},
    {"letter": "d", "number": "x"},
    {"letter": "ee", "number": 5},
    {"letter": "f", "number": 11},
    asdict(LetterNumber("g", 9)),
]

r = "\n".join([str(is_letter_number(f)) for f in letter_number_list])
print(r)
## ILN_Result(type_is=True,
## val=LetterNumber(letter='a', number=1))
## ILN_Result(type_is=False,
## val=TypeError("LetterNumber.__init__() got an
## unexpected keyword argument 'Letter'. Did you
## mean 'letter'?"))
## ILN_Result(type_is=False, val=TypeError("object
## of type 'int' has no len()"))
## ILN_Result(type_is=False, val=TypeError("'<'
## not supported between instances of 'int' and
## 'str'"))
## ILN_Result(type_is=False,
## val=ValueError('letter must be a single
## character string'))
## ILN_Result(type_is=False,
## val=ValueError('number must be an integer
## between 1 and 9'))
## ILN_Result(type_is=True,
## val=LetterNumber(letter='g', number=9))
