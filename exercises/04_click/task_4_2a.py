# -*- coding: utf-8 -*-
"""
Задание 4.2a

В этом задании вместо передачи параметров подключения через yaml, используются опции или запрос информации у пользователя.
Если параметры подключения отличаются от указанных в примерах ниже, надо изменить их в файле devices.yaml на свои, так как тест берет параметры из файла devices.yaml.

Создать интерфейс командной строки для скрипта:

* аргумент command - команда которую надо отправить на оборудование
* аргумент ip_list - один или более IP-адресов устройств к которым нужно подключиться
* опция --username, с коротким вариантом -u - имя пользователя. Если опция не указана при вызове скрипта, запросить ввод информации у пользователя (средствами click)
* опция --password, с коротким вариантом -p - пароль. Если опция не указана при вызове скрипта, запросить ввод информации у пользователя (средствами click). Скрывать ввод.
* опция --secret, с коротким вариантом -s - пароль на режим enable. Если опция не указана при вызове скрипта, запросить ввод информации у пользователя (средствами click). Скрывать ввод.
* опция --threads, с коротким вариантом -t - количество потоков. Значение по умолчанию - 5, диапазон возможных значений 1-10.

Применить декораторы к функции cli!

В функции cli должна вызываться функция send_command_to_devices с правильными аргументами:
список словарей с параметрами подключения к устройствам, команда, кол-во потоков.
Значения аргументов для функции send_command_to_devices должны быть получены из
аргументов скрипта (из click).

Help скрипта:

$ python task_4_2a.py --help
Usage: task_4_2a.py [OPTIONS] COMMAND IP_LIST...

Options:
  -u, --username TEXT
  -p, --password TEXT
  -s, --secret TEXT
  -t, --threads INTEGER RANGE  [default: 5]
  --help                       Show this message and exit.

Примеры использования скрипта:

$ python task_4_2a.py "sh clock" 192.168.100.1 192.168.100.2 -u cisco -p cisco -s cisco
['sh clock\r\n*07:38:07.767 UTC Fri Sep 11 2020\r\nR1#',
 'sh clock\r\n*07:38:07.813 UTC Fri Sep 11 2020\r\nR2#']

$ python task_4_2a.py "sh clock" 192.168.100.1 192.168.100.2 -u cisco
Password:
Secret:
['sh clock\r\n*07:38:07.767 UTC Fri Sep 11 2020\r\nR1#',
 'sh clock\r\n*07:38:07.813 UTC Fri Sep 11 2020\r\nR2#']

$ python task_4_2a.py "sh clock" 192.168.100.1
Username: cisco
Password:
Secret:
['sh clock\r\n*07:47:48.959 UTC Fri Sep 11 2020\r\nR1#']

$ python task_4_2a.py "sh clock" 192.168.100.1 192.168.100.2 -p cisco -s cisco
Username: cisco
['sh clock\r\n*08:12:07.102 UTC Fri Sep 11 2020\r\nR1#',
 'sh clock\r\n*08:12:07.143 UTC Fri Sep 11 2020\r\nR2#']

Функции send_show_command и send_command_to_devices менять нельзя.
Для правильной работы тестов надо написать в файле devices.yaml правильные параметры
подключения к оборудованию.

"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
import yaml
from cisco_telnet_class import CiscoTelnet


def send_show_command(device, command):
    with CiscoTelnet(**device) as t:
        output = t.send_show_command(command)
    return output


def send_command_to_devices(devices, command, threads=5):
    results = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(send_show_command, device, command) for device in devices
        ]
        for future in as_completed(futures):
            results.append(future.result())
    return results


# Это просто заготовка, чтобы не забыть, что click надо применять к этой функции
def cli():
    # pprint(send_command_to_devices(...))
    pass


if __name__ == "__main__":
    cli()
