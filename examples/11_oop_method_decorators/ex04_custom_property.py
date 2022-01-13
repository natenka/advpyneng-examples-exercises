from property_pure_python import MyProperty


class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self._private_mask = mask

    def __repr__(self):
        return f"IPAddress('{self.ip}', {self.mask})"

    def get_mask(self):
        print("get_mask")
        return self._private_mask

    def set_mask(self, new_mask):
        print("set_mask")
        if not isinstance(new_mask, int):
            raise TypeError("Маска должна быть числом")
        if new_mask not in range(33):
            raise ValueError("Маска должна быть в диапазоне 0-32")
        self._private_mask = new_mask

    mask = MyProperty(fget=get_mask, fset=set_mask)

