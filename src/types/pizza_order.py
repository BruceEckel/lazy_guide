# pizza_order.py
# Basic enumerations
from enum import Enum, auto
from dataclasses import dataclass


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


print(pizza := Pizza(Size.LARGE, [Add.PEPPERONI, Add.OLIVES]))
## Pizza(size=<Size.LARGE: 2>,
## toppings=[<Add.PEPPERONI: 1>, <Add.OLIVES: 3>])
print(pizza)
## Pizza(size=<Size.LARGE: 2>,
## toppings=[<Add.PEPPERONI: 1>, <Add.OLIVES: 3>])
print(order := Order(pizza))
## Ordered
print(order.update(Status.IN_OVEN))
## In Oven
print(order.update(Status.READY))
## Ready
