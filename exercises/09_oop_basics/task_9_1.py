# -*- coding: utf-8 -*-
"""
Задание 9.1

Создать класс IPv4Network, который представляет сеть.
При создании экземпляра класса, как аргумент обязательно передается
строка с адресом сети и маской, опционально gateway (gw) для сети.

Пример создания экземпляра класса:

In [1]: net1 = IPv4Network("10.1.1.0/29")

In [2]: net2 = IPv4Network("10.1.1.0/29", gw="10.1.1.1")

У каждого экземпляра класса IPv4Network должны быть такие переменные
(на примере экземпляра net1/net2):

* network - строка вида "10.1.1.0/29"
* broadcast - строка вида "10.1.1.7"
* gw - None или строка вида "10.1.1.1"
* hosts - кортеж со всеми IP-адресами указанной сети
  пример для net1 ('10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5', '10.1.1.6')
* allocated - множество IP-адресов, которые назначены на какие-то устройства в сети
* unassigned - множество со свободными IP-адресами

И такие методы:

* allocate_ip - ожидает как аргумент один IP-адрес. Если адрес входит в сеть экземпляра
  и еще не выделен, метод добавляет адрес в множество allocated (и удаляет из unassigned).
  Если адрес не из сети экземпляра, генерируется исключение ValueError. Если адрес уже
  находится в allocated, генерируется ValueError.
* free_ip - делает обратную операцию по сравнению с allocate_ip, аналогично работает с
  множествами allocated и unassigned. И генерирует ValueError при попытке освободить адрес,
  который и так свободен

Для реализации функционала класса можно использовать модуль ipaddress.
Ниже примеры работы с классом, чтобы немного облегчить его создание.

Пример создания экземпляра класса:

In [2]: net1 = IPv4Network('10.1.1.0/29')

После этого, должны быть доступны переменные экземпляра (gw в данном случае None):

In [3]: net1.network
Out[3]: '10.1.1.0/29'

In [4]: net1.broadcast
Out[4]: '10.1.1.7'

In [5]: net1.gw

In [6]: net1.allocated
Out[6]: set()

In [7]: net1.unassigned
Out[7]: {'10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5', '10.1.1.6'}

In [8]: net1.hosts
Out[8]: ('10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5', '10.1.1.6')


Метод allocate_ip ожидает как аргумент IP-адрес. Указанный адрес
должен быть записан в множество net1.allocated:

In [9]: net1 = IPv4Network('10.1.1.0/29', gw='10.1.1.1')

In [10]: net1.allocated
Out[10]: {'10.1.1.1'}

In [11]: net1.allocate_ip('10.1.1.6')

In [12]: net1.allocated
Out[12]: {'10.1.1.1', '10.1.1.6'}

In [13]: net1.unassigned
Out[13]: {'10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5'}

In [14]: net1.allocate_ip('10.1.1.3')

In [15]: net1.allocated
Out[15]: {'10.1.1.1', '10.1.1.3', '10.1.1.6'}

Генерация исключений при вызове net1.allocate_ip/net1.free_ip

In [16]: net1.allocated
Out[16]: {'10.1.1.1', '10.1.1.3', '10.1.1.6'}

In [17]: net1.allocate_ip('10.1.1.3')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-17-0f3a409c5b55> in <module>
----> 1 net1.allocate_ip('10.1.1.3')
...
ValueError: IP-адрес уже выделен

In [18]: net1.allocate_ip('10.1.1.103')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-18-e19e7d018a30> in <module>
----> 1 net1.allocate_ip('10.1.1.103')
...
ValueError: IP-адрес не входит в сеть 10.1.1.0/29

In [19]: net1.allocated
Out[19]: {'10.1.1.1', '10.1.1.3', '10.1.1.6'}

In [20]: net1.free_ip('10.1.1.3')

In [21]: net1.allocated
Out[21]: {'10.1.1.1', '10.1.1.6'}

In [22]: net1.free_ip('10.1.1.3')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-22-1ef45b9f8c9d> in <module>
----> 1 net1.free_ip('10.1.1.3')
...
ValueError: IP-адрес свободен

"""


if __name__ == "__main__":
    # Примеры обращения к переменным и вызова методов
    net1 = IPv4Network("10.1.1.0/29")
    # net1 = IPv4Network('10.1.1.0/29', gw="10.1.1.1")
    print(f"{net1.broadcast=}")
    print(f"{net1.hosts=}")
    print(f"{net1.allocated=}")
    print(f"{net1.unassigned=}")

    # allocate ip:
    print(f">>> {net1.allocate_ip('10.1.1.6')=}")
    print(f">>> {net1.allocate_ip('10.1.1.3')=}")
    print(f"{net1.allocated=}")
    print(f"{net1.unassigned=}")
    print(f"<<< {net1.free_ip('10.1.1.3')=}")
    print(f"{net1.allocated=}")
    print(f"{net1.unassigned=}")
    print(f">>> {net1.allocate_ip('10.1.1.3')=}")
    # print(f">>> {net1.allocate_ip('10.1.1.3')=}") # ValueError
    # print(f">>> {net1.allocate_ip('10.1.1.113')=}") # ValueError
    print(f"{net1.allocated=}")
    print(f"{net1.unassigned=}")
