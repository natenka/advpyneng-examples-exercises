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
import netdev
import itertools
import time


def spin():
    spinner = itertools.cycle('\|/-')
    while True:
        print(f'\r{next(spinner)} Waiting...', end='')
        time.sleep(0.1)


async def connect_ssh(device, command):
    await asyncio.sleep(7)
    print(f"\nПодключаюсь к {device['host']}")
    async with netdev.create(**device) as ssh:
        output = await ssh.send_command(command)
        await asyncio.sleep(5)
        print(f'\nПолучили данные от {device["host"]}')
    return output


device_params = {'host': '192.168.100.1',
                 'username': 'cisco',
                 'password': 'cisco',
                 'device_type': 'cisco_ios',
                 'secret': 'cisco'}


if __name__ == "__main__":
    asyncio.run(connect_ssh(device_params, 'sh clock'))

