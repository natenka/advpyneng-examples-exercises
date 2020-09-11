# -*- coding: utf-8 -*-
"""
Задание 13.2

Дополнить класс IPAddress: добавить метод, который позволит
выполнять сложение экземпляра класса IPAddress и числа.
В результате сложения должен возвращаться новый экземпляр класса IPAddress.

Пример создания экземпляра класса:
In [7]: ip1 = IPAddress('10.10.1.1', 24)

Суммирование:
In [8]: ip1
Out[8]: IPAddress(ip='10.10.1.1', mask=24)

In [9]: ip1 + 5
Out[9]: IPAddress(ip='10.10.1.6', mask=24)

In [10]: ip2 = ip1 + 5

In [11]: isinstance(ip2, IPAddress)
Out[11]: True

"""
import ipaddress
from dataclasses import dataclass, field


@dataclass(order=True)
class IPAddress:
    ip: str = field(compare=False)
    _ip: int = field(init=False, repr=False)
    mask: int

    def __post_init__(self):
        self._ip = int(ipaddress.ip_address(self.ip))
