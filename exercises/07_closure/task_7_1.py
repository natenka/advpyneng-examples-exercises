# -*- coding: utf-8 -*-
"""
Задание 7.1

Переделать функцию netmiko_ssh таким образом, чтобы при отправке строки "close",
вместо отправки "close" как команды на оборудование, закрывалось соединение к устройству
и выводилось сообщение 'Соединение закрыто'.

Пример работы функции:
In [1]: r1 = netmiko_ssh(**device_params)

In [2]: r1('sh clock')
Out[2]: '*08:07:44.267 UTC Thu Oct 17 2019'

In [3]: r1('close')
Соединение закрыто

Тест берет значения из словаря device_params в этом файле, поэтому если
для заданий используются другие адреса/логины, надо заменить их в словаре.
"""

from netmiko import ConnectHandler

device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}


def netmiko_ssh(**params_dict):
    ssh = ConnectHandler(**params_dict)
    ssh.enable()

    def send_show_command(command):
        return ssh.send_command(command)

    return send_show_command


if __name__ == "__main__":
    r1 = netmiko_ssh(**device_params)
    print(r1("sh clock"))
