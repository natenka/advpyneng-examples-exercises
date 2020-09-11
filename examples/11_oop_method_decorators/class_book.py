class Book:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    @property
    def total(self):
        return self.price * self.quantity


if __name__ == "__main__":
    good = Book("Good omens", 35, 100)
    print(good.total)
    good.price = 30
    print(good.total)
