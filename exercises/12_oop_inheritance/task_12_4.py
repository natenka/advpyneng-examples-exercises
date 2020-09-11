# -*- coding: utf-8 -*-
"""
Задание 12.4

Создать класс OrderingMixin, который будет автоматически добавлять к объекту методы:
* __ge__ - операция >=
* __ne__ - операция !=
* __le__ - операция <=
* __gt__ - операция >


OrderingMixin предполагает, что в классе уже определены методы:
* __eq__ - операция ==
* __lt__ - операция <

Проверить работу примеси можно на примере класса IPAddress. Определение класса можно менять.
OrderingMixin не должен использовать переменные класса IPAddress. Для работы методов
должны использоваться только существующие методы __eq__ и __lt__.
OrderingMixin должен работать и с любым другим классом у которого
есть методы __eq__ и __lt__.

Пример проверки методов с классом IPAddress:
In [4]: ip1 = IPAddress('10.10.1.1')

In [5]: ip2 = IPAddress('10.2.1.1')

In [6]: ip1 < ip2
Out[6]: False

In [7]: ip1 > ip2
Out[7]: True

In [8]: ip1 >= ip2
Out[8]: True

In [9]: ip1 <= ip2
Out[9]: False

In [10]: ip1 == ip2
Out[10]: False

In [11]: ip1 != ip2
Out[11]: True

"""
import ipaddress


class IPAddress:
    def __init__(self, ip):
        self._ip = int(ipaddress.ip_address(ip))

    def __str__(self):
        return f"IPAddress: {self._ip}"

    def __repr__(self):
        return f"IPAddress('{self._ip}')"

    def __eq__(self, other):
        return self._ip == other._ip

    def __lt__(self, other):
        return self._ip < other._ip
