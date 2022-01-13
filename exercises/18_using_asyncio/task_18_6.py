# -*- coding: utf-8 -*-
'''
Задание 18.6

Создать декоратор для сопрограмм retry, который выполняет декорируемую сопрограмму повторно,
заданное количество раз, если результат функции не был истинным.

Пример работы декоратора:
In [2]: @retry(times=3)
    ..: async def send_show(device, command):
    ..:     print(f'Подключаюсь к {device["host"]}')
    ..:     try:
    ..:         async with AsyncScrapli(**device) as conn:
    ..:             result = await conn.send_command(command)
    ..:             return result.result
    ..:     except ScrapliException as error:
    ..:         print(error, device["host"])


In [3]: send_show(device_params, 'sh clock')
Подключаюсь к 192.168.100.1
Out[3]: '*19:55:59.309 UTC Mon Nov 11 2019'


In [4]: device_params['password'] = '123123'

Обратите внимание, что если указано, что повторить попытку надо 3 раза,
то это три раза в дополнение к первому, то есть все подключение будет 4 раза:
In [5]: send_show(device_params, 'sh clock')
Подключаюсь к 192.168.100.1
Подключаюсь к 192.168.100.1
Подключаюсь к 192.168.100.1
Подключаюсь к 192.168.100.1

Проверить работу декоратора на сопрограмме send_show.

На каждой итерации должен проверяться результат функции. То есть не просто
повторяем вызов функции n раз, а каждый раз проверяем его и необходимость повторения.
'''
import asyncio
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException

device_params = {
    "host": "192.168.100.1",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_secondary": "cisco",
    "auth_strict_key": False,
    "timeout_socket": 5,
    "timeout_transport": 10,
    "platform": "cisco_iosxe",
    "transport": "asyncssh",
}


async def send_show(device, command):
    print(f'Подключаюсь к {device["host"]}')
    try:
        async with AsyncScrapli(**device) as conn:
            result = await conn.send_command(command)
            return result.result
    except ScrapliException as error:
        print(error, device["host"])


if __name__ == "__main__":
    output = asyncio.run(send_show(device_params, "show ip int br"))
    print(output)
