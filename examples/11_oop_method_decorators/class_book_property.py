## Стандартный вариант применения property без setter
class Book:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    # метод, который декорирован property становится getter'ом
    @property
    def total(self):
        print("getter")
        return self.price * self.quantity


## Стандартный вариант применения property с setter
class Book:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    # total остается атрибутом только для чтения
    @property
    def total(self):
        return round(self.price * self.quantity, 2)

    # а price доступен для чтения и записи
    @property  # этот метод превращается в getter
    def price(self):
        print("price getter")
        return self._price

    # при записи делается проверка значения
    @price.setter
    def price(self, value):
        print("price setter")
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if not value >= 0:
            raise ValueError("Значение должно быть положительным")
        self._price = float(value)


# Декораторы с явным getter
class Book:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    # создаем пустую property для total
    total = property()

    @total.getter
    def total(self):
        return round(self.price * self.quantity, 2)

    # создаем пустую property для price
    price = property()

    # позже указываем getter
    @price.getter
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


# property без декораторов
class Book:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def _get_total(self):
        return round(self.price * self.quantity, 2)

    def _get_price(self):
        print("price getter")
        return self._price

    def _set_price(self, value):
        print("price setter")
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if not value >= 0:
            raise ValueError("Значение должно быть положительным")
        self._price = float(value)

    total = property(_get_total)
    price = property(_get_price, _set_price)


# property без декораторов ver 2
class Book:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def _get_total(self):
        return round(self.price * self.quantity, 2)

    def _get_price(self):
        print("price getter")
        return self._price

    def _set_price(self, value):
        print("price setter")
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if not value >= 0:
            raise ValueError("Значение должно быть положительным")
        self._price = float(value)

    total = property()
    total = total.getter(_get_total)

    price = property()
    price = price.getter(_get_price)
    price = price.setter(_set_price)
