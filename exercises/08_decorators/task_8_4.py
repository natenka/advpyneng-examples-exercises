# -*- coding: utf-8 -*-
"""
Задание 8.4

Создать декоратор retry, который вызывает декорируемую функцию повторно,
заданное количество раз, если результат функции не был истинным.
При каждом повторном запуске результат проверяется:

* если он был истинным, он возвращается
* если нет, функция запускается повторно заданное количество раз

Если в любое из повторений результат истинный, надо вернуть результат
и больше не вызывать функцию повторно.

Пример работы декоратора:
In [2]: @retry(times=3)
    ..: def send_show_command(device, show_command):
    ..:     print('Подключаюсь к', device['host'])
    ..:     try:
    ..:         with ConnectHandler(**device) as ssh:
    ..:             ssh.enable()
    ..:             result = ssh.send_command(show_command)
    ..:         return result
    ..:     except SSHException:
    ..:         return None
    ..:

In [3]: send_show_command(device_params, 'sh clock')
Подключаюсь к 192.168.100.1
Out[3]: '*14:22:01.566 UTC Mon Mar 5 2018'

In [4]: device_params['password'] = '123123'

Обратите внимание, что если указано, что повторить попытку надо 3 раза,
то это три раза в дополнение к первому, то есть все подключение будет 4 раза:
In [5]: send_show_command(device_params, 'sh clock')
Подключаюсь к 192.168.100.1
Подключаюсь к 192.168.100.1
Подключаюсь к 192.168.100.1
Подключаюсь к 192.168.100.1

Тест проверяет декоратор на другой функции (не на send_show_command).
Значения в словаре device_params можно менять, если используются
другие адреса/логины.

Ограничение: Функцию send_show_command менять нельзя, можно только применить декоратор.
"""

from netmiko import (
    ConnectHandler,
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
)

device_params = {
    "device_type": "cisco_ios",
    "host": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}


def send_show_command(device, show_command):
    print("Подключаюсь к", device["host"])
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(show_command)
        return result
    except (NetMikoAuthenticationException, NetMikoTimeoutException) as error:
        print(error)


if __name__ == "__main__":
    output = send_show_command(device_params, "sh clock")
