#: pizza_order.py
# Basic enumerations
from enum import Enum, auto
from dataclasses import dataclass
from pprint import pp


class Size(Enum):
    SMALL = auto()
    LARGE = auto()


class Add(Enum):
    PEPPERONI = auto()
    MUSHROOMS = auto()
    OLIVES = auto()
    PEPPERS = auto()


@dataclass
class Pizza:
    size: Size
    toppings: list[Add]


class Status(Enum):
    ORDERED = auto()
    IN_OVEN = auto()
    READY = auto()


@dataclass
class Order:
    pizza: Pizza
    __status: Status = Status.ORDERED

    def __repr__(self) -> str:
        return self.__status.name.replace('_', ' ').title()

    def update(self, new_status: Status) -> "Order":
        self.__status = new_status
        return self


pizza = Pizza(Size.LARGE, [Add.PEPPERONI, Add.OLIVES])
pp(pizza, width=47)
pp(order := Order(pizza), width=47)
pp(order.update(Status.IN_OVEN), width=47)
pp(order.update(Status.READY), width=47)
