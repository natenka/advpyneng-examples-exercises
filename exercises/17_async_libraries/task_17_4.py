# -*- coding: utf-8 -*-
"""
Задание 17.4

Создать сопрограмму (coroutine) configure_router. Сопрограмма подключается
по SSH (с помощью scrapli) к устройству и выполняет перечень команд
в конфигурационном режиме на основании переданных аргументов.

При выполнении каждой команды, скрипт должен проверять результат на ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка, должно генерироваться
исключение ScrapliCommandFailure с информацией о том, какая ошибка возникла,
при выполнении какой команды и на каком устройстве. Шаблон сообщения:
'Команда "{}" выполнилась с ошибкой\n"{}" на устройстве {}'

Параметры функции:

* device - словарь с параметрами подключения к устройству
* config_commands - список команд или одна команда (строка), которые надо выполнить

Функция возвращает строку с результатами выполнения команды (вывод метода send_config(s)).
Функция должна перехватывать все остальные исключения scrapli, кроме ScrapliCommandFailure.

Пример вызова функции:

In [2]: asyncio.run(configure_router(devices[0], 'username user1 password daslfhjaklsdfhalsdh'))
Out[2]: 'username user1 password daslfhjaklsdfhalsdh\n'

In [3]: asyncio.run(configure_router(devices[0], correct_commands))
Out[3]: 'logging buffered 20010\nip http server\n'

Команды с ошибками:

In [4]: asyncio.run(configure_router(devices[0], 'usernme user1 password userpass'))
---------------------------------------------------------------------------
...
ScrapliCommandFailure: Команда "usernme user1 password userpass" выполнилась с ошибкой
"^
% Invalid input detected at '^' marker." на устройстве 192.168.100.1

In [5]: asyncio.run(configure_router(devices[0], commands_with_errors))
---------------------------------------------------------------------------
...
ScrapliCommandFailure: Команда "logging 0255.255.1" выполнилась с ошибкой
"^
% Invalid input detected at '^' marker." на устройстве 192.168.100.1

In [6]: asyncio.run(configure_router(devices[0], commands_with_errors[1:]))
---------------------------------------------------------------------------
...
ScrapliCommandFailure: Команда "logging" выполнилась с ошибкой
"% Incomplete command." на устройстве 192.168.100.1


Запустить сопрограмму и проверить, что она работает корректно с одним из устройств
в файле devices_scrapli.yaml.

При необходимости, можно использовать функции из предыдущих заданий
и создавать дополнительные функции.

Для заданий в этом разделе нет тестов!
"""

# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]

import asyncio
import yaml



if __name__ == '__main__':
    with open('devices_scrapli.yaml') as f:
        devices = yaml.safe_load(f)
    # примеры вызова функции (не будут работать до выполнения задания)
    print(asyncio.run(configure_router(devices[0], correct_commands + commands_with_errors)))
    print(asyncio.run(configure_router(devices[0], correct_commands)))
    print(asyncio.run(configure_router(devices[0], commands_with_errors[1])))

