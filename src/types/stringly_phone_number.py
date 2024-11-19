#: stringly_phone_number.py
import re
from typing import Optional


def validate_number(phone: str) -> bool:
    pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
    return bool(re.match(pattern, phone))


def format_number(phone: str) -> Optional[str]:
    if not validate_number(phone):
        print(f"Invalid: {phone}")
        return None
    return f"Number: {phone}"


def is_us_number(phone: str) -> bool:
    if not validate_number(phone):
        print(f"Invalid: {phone}")
        return False
    return True


formatted_number = format_number("(123) 456-7890")
if formatted_number:
    print(formatted_number)

n = "123-456-7890"
print(f"{n} is a valid US number: {is_us_number(n)}")
