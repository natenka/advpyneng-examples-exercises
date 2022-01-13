class Typed:
    attr_type = object

    def __set_name__(self, owner, attr_name):
        print(f"set_name {owner=} {attr_name=}")
        self.name = attr_name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.attr_type):
            raise TypeError(f'Wrong data type, expected {self.attr_type}')
        instance.__dict__[self.name] = value

class Integer(Typed):
    attr_type = int

class String(Typed):
    attr_type = str


class Book:
    price = Integer()
    quantity = Integer()
    title = String()

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

