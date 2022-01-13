import random


class Property:
    def __init__(self, fget=None, fset=None, fdel=None):
        print("Property init")
        self.fget = fget
        self.fset = fset
        self.id = random.random()

    def __get__(self, instance, instancetype=None):
        print("Property get", f"\n{self=}\n{instance=}\n{instancetype=}")
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        print("Property set")
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __repr__(self):
        return f"<Property {self.id}>"

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
        self._mask = new_mask

    mask = Property(_get_mask, _set_mask)

