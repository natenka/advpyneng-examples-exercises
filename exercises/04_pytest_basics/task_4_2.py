# -*- coding: utf-8 -*-
"""
Задание 4.2

Написать тесты для класса Network. Тесты должны проверять:

* атрибут network и атрибут addresses:

  * наличие атрибута
  * правильное содержание

* метод __iter__:

  * метод есть
  * что он возвращает итератор
  * что при итерации возвращаются IP-адреса и правильные IP-адреса (достаточно проверить 2 адреса)

* метод __len__:

  * проверка количества IP-адресов

* метод __getitem__:

  * проверить обращение по положительному, отрицательному индексу
  * проверить, что при обращении к не существующему индексу, генерируется исключение IndexError


Тесты написать в файле заданий. Разделить на тесты по своему усмотрению.
"""
import ipaddress


class Network:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = tuple([str(ip) for ip in subnet.hosts()])

    def __iter__(self):
        return iter(self.addresses)

    def __len__(self):
        return len(self.addresses)

    def __getitem__(self, index):
        return self.addresses[index]


# пример создания экземпляра
# net1 = Network('10.1.1.192/30')
