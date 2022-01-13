import ipaddress
from functools import wraps


def verbose(func):
    print("Декорируем функцию")

    def inner(*args, **kwargs):
        print(f"Вызываю функцию {func.__name__}")
        return func(*args, **kwargs)

    return inner


def verbose_methods(cls):
    for name, value in vars(cls).items():
        if callable(value) and name not in ("__str__", "__repr__"):
            setattr(cls, name, verbose(value))
    return cls


@verbose_methods
class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        print("############ str")
        return f"IPAddress: {self.ip}"

    def __repr__(self):
        return f"IPAddress('{self.ip}')"

    def test(self, value):
        pass
