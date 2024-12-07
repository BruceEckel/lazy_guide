#: pizza_order.py
# Basic enumerations
from enum import Enum, auto
from dataclasses import dataclass


class Size(Enum):
    SMALL = auto()
    LARGE = auto()


class Add(Enum):
    PEPPERONI = auto()
    MUSHROOMS = auto()
    BLACK_OLIVES = auto()
    GREEN_PEPPERS = auto()


@dataclass
class Pizza:
    size: Size
    toppings: list[Add]

    # def describe(self) -> str:
    #     toppings_list = ', '.join(topping.name.replace("_", " ").title() for topping in self.toppings)
    #     return f"Pizza Size: {self.size.name.replace('_', ' ').title()}, Toppings: {toppings_list}"


class Status(Enum):
    ORDERED = auto()
    IN_OVEN = auto()
    READY = auto()


@dataclass
class Order:
    pizza: Pizza
    __status: Status = Status.ORDERED

    def __str__(self) -> str:
        return self.__status.name.replace('_', ' ').title()

    def update(self, new_status: Status) -> "Order":
        self.__status = new_status
        return self


pizza = Pizza(size=Size.LARGE, toppings=[Add.PEPPERONI, Add.MUSHROOMS, Add.GREEN_PEPPERS])
print(pizza)

order = Order(pizza=pizza)
print(order)
print(order.update(Status.IN_OVEN))
print(order.update(Status.READY))
