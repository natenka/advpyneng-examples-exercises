# -*- coding: utf-8 -*-
"""
Задание 16.3

Написать аннотацию для всех методов класса PingNetwork:
аннотация должна описывать параметры и возвращаемое значение.

Проверить код с помощью mypy, если возникли какие-то ошибки, исправить их.

Для заданий в этом разделе нет тестов!
"""

import subprocess
from concurrent.futures import ThreadPoolExecutor
from task_16_2 import IPv4Network


class PingNetwork:
    def __init__(self, network):
        self.network = network

    def _ping(self, ip):
        result = subprocess.run(['ping', '-c', '3', '-n', ip],
                            stdout=subprocess.DEVNULL)
        ip_is_reachable = result.returncode == 0
        return ip_is_reachable

    def scan(self, workers=5, include_unassigned=False):
        ip_to_ping = self.network.allocated
        if include_unassigned:
            ip_to_ping.extend(self.network.unassigned())
        reachable = []
        unreachable = []

        with ThreadPoolExecutor(max_workers=workers) as executor:
            results = executor.map(self._ping, ip_to_ping)
        for ip, status in zip(ip_to_ping, results):
            if status:
                reachable.append(ip)
            else:
                unreachable.append(ip)
        return reachable, unreachable


if __name__ == "__main__":
    net1 = IPv4Network('8.8.4.0/29')
    print(net1.hosts())
    net1.allocate('8.8.4.2')
    net1.allocate('8.8.4.4')
    net1.allocate('8.8.4.6')
    print('Allocated hosts:', net1.allocated)
    ping = PingNetwork(net1)
    print(ping.scan())

