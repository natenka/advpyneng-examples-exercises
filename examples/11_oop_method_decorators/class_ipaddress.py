## Стандартный вариант применения property без setter
class IPAddress:
    def __init__(self, ip, mask):
        self._ip = ip
        self._mask = mask

    # метод, который декорирован property становится getter'ом
    @property
    def mask(self):
        print("getter")
        return self._mask


## Стандартный вариант применения property с setter
class IPAddress:
    def __init__(self, ip, mask):
        self._ip = ip
        self._mask = mask

    @property  # этот метод превращается в getter
    def mask(self):
        print("getter")
        return self._mask

    @mask.setter
    def mask(self, value):
        print("setter")
        if not isinstance(value, int):
            raise TypeError("Значение должно быть числом")
        if not 8 <= value <= 32:
            raise ValueError("Значение должно быть в диапазоне 8 - 32")
        self._mask = value


### Больше примеров property в файле class_book_property.py
