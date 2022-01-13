from dataclasses import field
from typing import Optional
from pydantic.dataclasses import dataclass

@dataclass
class Book:
    title: str
    price: int
    quantity: Optional[int] = 0
    _price: int = field(init=False, repr=False)

    @property
    def total(self):
        return self.price * self.quantity

    @property
    def price(self):
        print("price getter")
        return self._price

    @price.setter
    def price(self, value):
        print("price setter")
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if not value >= 0:
            raise ValueError("Значение должно быть положительным")
        self._price = float(value)



book1 = Book("Good Omens", "24", 1000)
