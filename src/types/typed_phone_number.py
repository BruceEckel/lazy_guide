# typed_phone_number.py
import re
from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class PhoneNumber:
    original: str
    country: Optional[int] = field(init=False, default=None)
    area: int = field(init=False)
    exchange: int = field(init=False)
    line: int = field(init=False)
    ext: Optional[int] = field(init=False, default=None)

    def __post_init__(self):
        # Different possible phone number formats
        patterns = [
            # +Country Code (XXX) XXX-XXXX ext. XXXX:
            r"^\+?(\d{1,3}) \((\d{3})\) (\d{3})-(\d{4})(?: ext\. (\d+))?$",
            # (XXX) XXX-XXXX ext. XXXX:
            r"^\((\d{3})\) (\d{3})-(\d{4})(?: ext\. (\d+))?$",
            # XXX-XXX-XXXX ext. XXXX:
            r"^(\d{3})-(\d{3})-(\d{4})(?: ext\. (\d+))?$",
            # XXXXXXXXXX (10-digit number):
            r"^(\d{10})$"
        ]

        match = None
        for pattern in patterns:
            match = re.match(pattern, self.original)
            if match:
                break

        if not match:
            raise ValueError(
                f"Invalid: {self.original}"
            )

        # Assign attributes for frozen dataclass
        def assign(attr_name: str, value: Optional[int]):
            object.__setattr__(self, attr_name, value)

        if len(match.groups()) == 5:  # Country code
            assign('country', int(match.group(1)))
            assign('area', int(match.group(2)))
            assign('exchange', int(match.group(3)))
            assign('line', int(match.group(4)))
            if match.group(5):
                assign('ext', int(match.group(5)))
        elif len(match.groups()) == 4:  # No country code
            assign('area', int(match.group(1)))
            assign('exchange', int(match.group(2)))
            assign('line', int(match.group(3)))
            if match.group(4):
                assign('ext', int(match.group(4)))
        elif len(match.groups()) == 1:  # 10-digit number
            assign('area', int(self.original[:3]))
            assign('exchange', int(self.original[3:6]))
            assign('line', int(self.original[6:]))

    def __str__(self) -> str:
        return (
            f"{f'+{self.country} ' if self.country else ''}"
            f"({self.area}) "
            f"{self.exchange}-{self.line}"
            f"{f' ext. {self.ext}' if self.ext else ''}"
        )


def call(number: PhoneNumber):
    print(number)


def text(number: PhoneNumber, message: str):
    print(number, message)


for n in ["+1 (123) 456-7890",
          "(123) 456-7890",
          "123-456-7890",
          "123-456-7890 ext. 22",
          "1234567890",
          ]:
    call(PhoneNumber(n))
    text(PhoneNumber(n), "Howdy!")
## +1 (123) 456-7890
## +1 (123) 456-7890 Howdy!
## (123) 456-7890
## (123) 456-7890 Howdy!
## (123) 456-7890
## (123) 456-7890 Howdy!
## (123) 456-7890 ext. 22
## (123) 456-7890 ext. 22 Howdy!
## (123) 456-7890
## (123) 456-7890 Howdy!
