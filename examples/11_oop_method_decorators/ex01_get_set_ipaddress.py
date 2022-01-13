class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.set_mask(mask)

    def get_mask(self):
        print("get")
        return self._private_mask

    def set_mask(self, new_mask):
        print("set")
        if not isinstance(new_mask, int):
            raise TypeError("Маска должна быть числом")
        if new_mask not in range(33):
            raise ValueError("Маска должна быть в диапазоне 0-32")
        self._private_mask = new_mask


ip1 = IPAddress("10.1.1.1", 24)
