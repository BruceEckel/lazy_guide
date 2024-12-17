# stringly_phone_number.py
import re


def call(phone: str):
    if not re.match(r"^\(\d{3}\) \d{3}-\d{4}$", phone):
        print(f"Bad number: {phone}")
    else:
        print(phone)


def text(phone: str, message: str):
    if not re.match(r"^\(\d{3}\) \d{3}-\d{4}$", phone):
        print(f"Bad number: {phone}")
    else:
        print(phone, message)


call("(123) 456-7890")
## (123) 456-7890
text("(123) 456-7890", "Howdy!")
## (123) 456-7890 Howdy!
text("123-456-7890", "Hi!")
## Bad number: 123-456-7890
