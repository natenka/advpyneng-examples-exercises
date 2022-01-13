class Integer:
    def __init__(self, attr_name):
        self.name = attr_name

    def __get__(self, instance, cls):
        print(f"__get__  {instance=} {cls=}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"__set__  {instance=} {value=}")
        if not isinstance(value, int):
            raise TypeError("Значение должно быть числом")
        if not value >= 0:
            raise ValueError("Значение должно быть положительным")
        instance.__dict__[self.name] = value


class Book:
    price = Integer("price")
    quantity = Integer("quantity")

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity


class IPAddress:
    mask = Integer("mask")


