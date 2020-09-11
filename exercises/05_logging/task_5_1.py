# -*- coding: utf-8 -*-
"""
Задание 5.1

Добавить логирование в скрипт с выводом информации на стандартный поток вывода.
Формат логов и сообщения надо определить из примеров вывода ниже. Кроме того,
это должен быть единственный вывод модуля logging, сообщения других модулей надо выводить только если их уровень WARNING.


Пример вывода при успешном подключении на все три устройства:
$ python task_5_1.py
ThreadPoolExecutor-0_0 2020-09-11 10:06:01,385 root DEBUG: Подключение к 192.168.100.1
ThreadPoolExecutor-0_1 2020-09-11 10:06:01,392 root DEBUG: Подключение к 192.168.100.2
ThreadPoolExecutor-0_2 2020-09-11 10:06:01,394 root DEBUG: Подключение к 192.168.100.3
ThreadPoolExecutor-0_1 2020-09-11 10:06:02,686 root DEBUG: Получен ответ от 192.168.100.2
ThreadPoolExecutor-0_0 2020-09-11 10:06:02,762 root DEBUG: Получен ответ от 192.168.100.1
ThreadPoolExecutor-0_2 2020-09-11 10:06:02,857 root DEBUG: Получен ответ от 192.168.100.3
{'192.168.100.1': '*10:06:02.518 UTC Fri Sep 11 2020',
 '192.168.100.2': '*10:06:02.445 UTC Fri Sep 11 2020',
 '192.168.100.3': '*10:06:02.628 UTC Fri Sep 11 2020'}


Пример вывода при ошибке аутентификации на первом устройстве (неправильный пароль):
$ python task_5_1.py
ThreadPoolExecutor-0_0 2020-09-11 10:07:24,867 root DEBUG: Подключение к 192.168.100.1
ThreadPoolExecutor-0_1 2020-09-11 10:07:24,875 root DEBUG: Подключение к 192.168.100.2
ThreadPoolExecutor-0_2 2020-09-11 10:07:24,878 root DEBUG: Подключение к 192.168.100.3
ThreadPoolExecutor-0_1 2020-09-11 10:07:26,138 root DEBUG: Получен ответ от 192.168.100.2
ThreadPoolExecutor-0_2 2020-09-11 10:07:26,252 root DEBUG: Получен ответ от 192.168.100.3
ThreadPoolExecutor-0_0 2020-09-11 10:07:27,775 root WARNING: Authentication failed.
{'192.168.100.1': AuthenticationException('Authentication failed.'),
 '192.168.100.2': '*10:07:25.909 UTC Fri Sep 11 2020',
 '192.168.100.3': '*10:07:26.014 UTC Fri Sep 11 2020'}


Пример вывода при ошибке перехода в enable на первом устройстве (неправильный пароль на enable):
$ python task_5_1.py
ThreadPoolExecutor-0_0 2020-09-11 10:07:52,096 root DEBUG: Подключение к 192.168.100.1
ThreadPoolExecutor-0_1 2020-09-11 10:07:52,102 root DEBUG: Подключение к 192.168.100.2
ThreadPoolExecutor-0_2 2020-09-11 10:07:52,104 root DEBUG: Подключение к 192.168.100.3
ThreadPoolExecutor-0_1 2020-09-11 10:07:53,462 root DEBUG: Получен ответ от 192.168.100.2
ThreadPoolExecutor-0_2 2020-09-11 10:07:53,589 root DEBUG: Получен ответ от 192.168.100.3
ThreadPoolExecutor-0_0 2020-09-11 10:08:13,343 root WARNING: Не получилось перейти в режим enable
{'192.168.100.1': ValueError("Failed to enter enable mode. Please ensure you pass the 'secret' argument to ConnectHandler."),
 '192.168.100.2': '*10:07:53.219 UTC Fri Sep 11 2020',
 '192.168.100.3': '*10:07:53.347 UTC Fri Sep 11 2020'}

Пример вывода при недоступном IP-адресе:
$ python task_5_1.py
ThreadPoolExecutor-0_0 2020-09-11 10:09:08,922 root DEBUG: Подключение к 192.168.100.13
ThreadPoolExecutor-0_1 2020-09-11 10:09:08,926 root DEBUG: Подключение к 192.168.100.2
ThreadPoolExecutor-0_2 2020-09-11 10:09:08,928 root DEBUG: Подключение к 192.168.100.3
ThreadPoolExecutor-0_2 2020-09-11 10:09:10,170 root DEBUG: Получен ответ от 192.168.100.3
ThreadPoolExecutor-0_1 2020-09-11 10:09:10,185 root DEBUG: Получен ответ от 192.168.100.2
ThreadPoolExecutor-0_0 2020-09-11 10:09:13,932 root WARNING: TCP connection to device failed.

Common causes of this problem are:
1. Incorrect hostname or IP address.
2. Wrong TCP port.
3. Intermediate firewall blocking access.

Device settings: cisco_ios 192.168.100.13:22


{'192.168.100.13': NetmikoTimeoutException('TCP connection to device failed.\n\nCommon causes of this problem are:\n1. Incorrect hostname or IP address.\n2. Wrong TCP port.\n3. Intermediate firewall blocking access.\n\nDevice settings: cisco_ios 192.168.100.13:22\n\n'),
 '192.168.100.2': '*10:09:09.946 UTC Fri Sep 11 2020',
 '192.168.100.3': '*10:09:09.945 UTC Fri Sep 11 2020'}


Для заданий этого раздела нет тестов.
"""

from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from itertools import repeat
import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import SSHException


def send_show(device_dict, command):
    ip = device_dict["host"]
    try:
        with ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result
    except SSHException as error:
        return error
    except ValueError as error:
        return error


def send_command_to_devices(devices, command, max_workers=5):
    data = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for device, output in zip(devices, result):
            data[device["host"]] = output
    return data


if __name__ == "__main__":
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    pprint(send_command_to_devices(devices, "sh clock"))
