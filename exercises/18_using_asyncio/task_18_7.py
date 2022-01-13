# -*- coding: utf-8 -*-
'''
Задание 18.7


Создать сопрограмму (coroutine) spin. Сопрограмма должна работать бесконечно
и постоянно отображать spinner. Пример синхронного варианта функции показан ниже
и его можно взять за основу для асинхронного:

In [1]: import itertools
   ...: import time
   ...:
   ...: def spin():
   ...:     spinner = itertools.cycle('\|/-')
   ...:     while True:
   ...:         print(f'\r{next(spinner)} Waiting...', end='')
   ...:         time.sleep(0.1)
   ...:

In [3]: spin()
/ Waiting...
...
KeyboardInterrupt:

In [4]:

Создать декоратор для сопрограмм spinner, который запускает сопрограмму spin на время работы
декорируемой функции и останавливает его, как только функция закончила работу.
Проверить работу декоратора на сопрограмме connect_ssh.

Чтобы показать работу декоратора, записано видео с запуском декорированной функции:
https://youtu.be/YdeUxrlbAwk

Подсказка: задачи (task) можно отменять методом cancel.

При необходимости, можно использовать функции из предыдущих заданий
и создавать дополнительные функции.

Для заданий в этом разделе нет тестов!
'''
import asyncio
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
import itertools
import time


def spin():
    spinner = itertools.cycle('\|/-')
    while True:
        print(f'\r{next(spinner)} Waiting...', end='')
        time.sleep(0.1)


async def send_show(device, command):
    print(f'Подключаюсь к {device["host"]}')
    try:
        async with AsyncScrapli(**device) as conn:
            result = await conn.send_command(command)
            return result.result
    except ScrapliException as error:
        print(error, device["host"])


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


if __name__ == "__main__":
    output = asyncio.run(send_show(device_params, "show ip int br"))
    print(output)
