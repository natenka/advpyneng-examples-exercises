# -*- coding: utf-8 -*-
"""
Задание 13.3

Дополнить класс Book: добавить метод to_dict.
Метод to_dict должен возвращать словарь в котором:
    ключи - имена переменных экземпляра
    значения - значения переменных

В словаре должны быть все переменные, кроме тех, которые начинаются на _.
Словарь надо получить динамически, не прописывая каждый атрибут вручную.

Пример создания экземпляра класса:
In [4]: b1 = Book('Good Omens', 35, 5)

В этом случае должен возвращаться такой словарь:
In [5]: b1.to_dict()
Out[5]: {'price': 35.0, 'quantity': 5, 'title': 'Good Omens', 'total': 175.0}


Обратите внимание, что в словаре не только простые переменные, но и переменные,
которые созданы через property.

"""
from dataclasses import dataclass, field


@dataclass
class Book:
    title: str
    price: float
    _price: float = field(init=False, repr=False)
    quantity: int = 0

    @property
    def total(self):
        return round(self.price * self.quantity, 2)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if not value >= 0:
            raise ValueError("Значение должно быть положительным")
        self._price = float(value)
