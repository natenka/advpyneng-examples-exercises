# -*- coding: utf-8 -*-
"""
Задание 16.2

Написать аннотацию для всех методов класса IPv4Network:
аннотация должна описывать параметры и возвращаемое значение.

Проверить код с помощью mypy, если возникли какие-то ошибки, исправить их.

Для заданий в этом разделе нет тестов!
"""

import ipaddress


class IPv4Network:
    def __init__(self, network):
        self._net = ipaddress.ip_network(network)
        self.address = str(self._net.network_address)
        self.mask = self._net.prefixlen
        self.broadcast = str(self._net.broadcast_address)
        self.allocated = []

    def hosts(self):
        return [str(ip) for ip in self._net.hosts()]

    def allocate(self, ip):
        self.allocated.append(ip)

    def unassigned(self):
        return [ip for ip in self.hosts() if ip not in self.allocated]


if __name__ == "__main__":
    net1 = IPv4Network("10.1.1.0/28")
    all_hosts = net1.hosts()
    net1.allocate("10.1.1.1")
    net1.allocate("10.1.1.4")
    print(net1.allocated)
