class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    @property
    def mask(self):
        print("get")
        return self._private_mask
    # mask = property(mask)

    @mask.setter
    def mask(self, new_mask):
        print("set")
        if not isinstance(new_mask, int):
            raise TypeError("Маска должна быть числом")
        if new_mask not in range(33):
            raise ValueError("Маска должна быть в диапазоне 0-32")
        self._private_mask = new_mask
    # mask = mask.setter(mask)

    def __repr__(self):
        return f"IPAddress('{self.ip}', {self.mask})"

