# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать сопрограмму (coroutine) send_config_commands. Сопрограмма
должна подключаться по SSH с помощью asyncssh к одному устройству,
переходить в режим enable, в конфигурационный режим, выполнять указанные команды,
а затем выходить из конфигурационного режима.

Параметры функции:

* host - IP-адрес устройства
* username - имя пользователя
* password - пароль
* enable_password - пароль на режим enable
* config_commands - список команд или одна команда (строка), которые надо выполнить

Функция возвращает строку с результатами выполнения команды:

In [1]: import asyncio

In [2]: from task_17_1 import send_config_commands

In [3]: commands = ['interface loopback55', 'ip address 10.5.5.5 255.255.255.255']

In [4]: print(asyncio.run(send_config_commands('192.168.100.1', 'cisco', 'cisco', 'cisco', commands)))
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#interface loopback55
R1(config-if)#ip address 10.5.5.5 255.255.255.255
R1(config-if)#end
R1#

In [5]: asyncio.run(send_config_commands(**r1, config_commands=commands))
Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loopback55\r\nR1(config-if)#ip address 10.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'


Запустить сопрограмму и проверить, что она работает корректно.
При необходимости можно создавать дополнительные функции.

Для заданий в этом разделе нет тестов!
"""
import asyncio
import asyncssh


r1 = {
    "host": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "enable_password": "cisco",
}
