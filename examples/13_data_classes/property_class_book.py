from property_descriptor import MyProperty


class Book:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def _get_price(self):
        print("Book: price getter")
        return self._price

    def _set_price(self, value):
        print("Book: price setter")
        if value < 0:
            raise ValueError("Error")
        self._price = value

    price = MyProperty(fset=_set_price)

    def __repr__(self):
        return f"Book(title={self.title})"
