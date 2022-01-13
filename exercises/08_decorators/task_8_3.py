# -*- coding: utf-8 -*-
"""
Задание 8.3

Создать декоратор add_verbose, который добавляет в функцию
дополнительный параметр verbose.
Когда параметру передано значение True, на стандартный поток вывода
должна отображаться информация о вызове функции и ее аргументах
(пример работы декоратора показан ниже).

По умолчанию, значение параметра должно быть равным False.

Проверить работу декоратора на функции send_show_command.

Пример вывода:
In [3]: @add_verbose
   ...: def send_show_command(params, command):
   ...:     with ConnectHandler(**params) as ssh:
   ...:         ssh.enable()
   ...:         result = ssh.send_command(command)
   ...:     return result
   ...:

In [4]: print(send_show_command(device_params, 'sh clock', verbose=True))
Вызываем send_show_command
Позиционные аргументы: ({'device_type': 'cisco_ios', 'host': '192.168.100.1', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'}, 'sh clock')
*14:01:07.353 UTC Mon Feb 26 2018

In [5]: print(send_show_command(device_params, 'sh clock', verbose=True))
Вызываем send_show_command
Позиционные аргументы: ({'device_type': 'cisco_ios', 'host': '192.168.100.1', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'}, 'sh clock')
*15:09:45.152 UTC Fri Oct 18 2019

In [6]: print(send_show_command(device_params, command='sh clock', verbose=True))
Вызываем send_show_command
Позиционные аргументы: ({'device_type': 'cisco_ios', 'host': '192.168.100.1', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'},)
Ключевые аргументы: {'command': 'sh clock'}
*15:10:09.222 UTC Fri Oct 18 2019

In [7]: print(send_show_command(params=device_params, command='sh clock', verbose=True))
Вызываем send_show_command
Ключевые аргументы: {'params': {'device_type': 'cisco_ios', 'host': '192.168.100.1', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'}, 'command': 'sh clock'}
*15:10:28.524 UTC Fri Oct 18 2019

In [8]: print(send_show_command(device_params, 'sh clock', verbose=False))
*14:01:18.141 UTC Mon Feb 26 2018


Тест проверяет декоратор на другой функции (не на send_show_command).
Значения в словаре device_params можно менять, если используются
другие адреса/логины.

Ограничение: Функцию send_show_command менять нельзя, можно только применить декоратор.
"""

from netmiko import ConnectHandler

device_params = {
    "device_type": "cisco_ios",
    "host": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}


def send_show_command(params, command):
    with ConnectHandler(**params) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result
