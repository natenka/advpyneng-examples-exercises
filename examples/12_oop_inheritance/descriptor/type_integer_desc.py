class Integer:

    def __set_name__(self, owner, name):
        print("Integer __set_name__")
        print(f"__setname__ {self=} {owner=} {name=}")
        self.name = name

    def __get__(self, instance, cls):
        print(f"__get__ {self=} {instance=} {cls=}")
        return instance.__dict__[f"_{self.name}"]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Значение должно быть числом")
        print(f"__set__ {self=} {instance=} {value=}")
        instance.__dict__[f"_{self.name}"] = value


class IPAddress:
    mask = Integer()

    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask
