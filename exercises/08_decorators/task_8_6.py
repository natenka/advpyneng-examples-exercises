# -*- coding: utf-8 -*-
"""
Задание 8.6

Создать декоратор total_order, который добавляет к классу методы:

* __ge__ - операция >=
* __ne__ - операция !=
* __le__ - операция <=
* __gt__ - операция >


Декоратор total_order полагается на то, что в классе уже определены методы:
* __eq__ - операция ==
* __lt__ - операция <

Если методы __eq__ и __lt__ не определены, сгенерировать исключение ValueError при декорации.

Проверить работу декоратора можно на примере класса IPAddress. Класс нельзя менять,
можно только декорировать.
Декоратор не должен использовать переменные класса/экземпляров IPAddress. Для работы методов
должны использоваться только существующие методы __eq__ и __lt__.
Декоратор должен работать и с любым другим классом у которого
есть методы __eq__ и __lt__.


Пример проверки методов с классом IPAddress после декорирования:
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
        self.ip = ip

    def __repr__(self):
        return f"IPAddress('{self.ip}')"

    def __eq__(self, other):
        return self._ip == other._ip

    def __lt__(self, other):
        return self._ip < other._ip

