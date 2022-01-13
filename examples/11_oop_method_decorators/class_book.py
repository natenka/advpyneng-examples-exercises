class Book:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    @property
    def total(self):
        print("getter total")
        return self.price * self.quantity

    @property
    def price(self):
        print("getter price")
        return self._price

    @price.setter
    def price(self, new_price):
        print("setter price")
        if not isinstance(new_price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if not new_price >= 0:
            raise ValueError("Значение цены должно быть больше 0")
        self._price = new_price


if __name__ == "__main__":
    good = Book("Good omens", 35, 100)
    print(good.total)
    good.price = 30
    print(good.total)
