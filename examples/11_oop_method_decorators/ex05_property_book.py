class Book:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    @property
    def total(self):
        return round(self.price * self.quantity, 2)

    @property  # этот метод превращается в getter
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

