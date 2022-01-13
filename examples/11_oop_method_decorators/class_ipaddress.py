# Вариант без property
class OldIPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self._mask = mask

    def get_mask(self):
        print("Mask property")
        return self._mask

    def set_mask(self, new_mask):
        print("Mask setter")
        if not isinstance(new_mask, int):
            raise TypeError("Маска должна быть числом")
        if new_mask not in range(8, 31):
            raise ValueError("Значение маски должно быть от 8 до 30")
        self._mask = new_mask



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


# проверка в init
class IPAddress:
    def __init__(self, ip, mask):
        self._ip = ip
        self.mask = mask

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


# создание getter явно
class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    mask = property()

    @mask.getter
    def mask(self):
        print("Mask getter")
        return self._mask

    @mask.setter
    def mask(self, new_mask):
        print("Mask setter")
        if not isinstance(new_mask, int):
            raise TypeError("Маска должна быть числом")
        if new_mask not in range(8, 31):
            raise ValueError("Значение маски должно быть от 8 до 30")
        self._mask = new_mask


# создание property без декоратора
class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    def _get_mask(self):
        print("Mask getter")
        return self._mask

    def _set_mask(self, new_mask):
        print("Mask setter")
        if not isinstance(new_mask, int):
            raise TypeError("Маска должна быть числом")
        if new_mask not in range(8, 31):
            raise ValueError("Значение маски должно быть от 8 до 30")
        self._mask = new_mask

    mask = property(_get_mask, _set_mask)

### Больше примеров property в файле class_book_property.py
