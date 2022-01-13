# -*- coding: utf-8 -*-
"""
Задание 4.2b

Скопировать функцию cli и настройку click из задания 4.2a.
Добавить флаг --timed, при указании которого, время выполнения скрипта
засекается и выводится на стандартный поток вывода.

В функции cli должна вызываться функция send_command_to_devices с правильными аргументами:
список словарей с параметрами подключения к устройствам, команда, кол-во потоков.
Значения аргументов для функции send_command_to_devices должны быть получены из
аргументов скрипта (из click).

Help скрипта
$ python task_4_2b.py --help
Usage: task_4_2b.py [OPTIONS] COMMAND IP_LIST...

Options:
  -u, --username TEXT
  -p, --password TEXT
  -s, --secret TEXT
  -t, --threads INTEGER RANGE
  --timed
  --help                       Show this message and exit.

Пример вызова:

$ python task_4_2b.py "sh clock" 192.168.100.1 192.168.100.2 192.168.100.3 -t 1 --timed
Username: cisco
Password:
Secret:
['sh clock\r\n*08:31:40.684 UTC Fri Sep 11 2020\r\nR1#',
 'sh clock\r\n*08:31:41.742 UTC Fri Sep 11 2020\r\nR2#',
 'sh clock\r\n*08:31:42.802 UTC Fri Sep 11 2020\r\nR3#']

Время выполнения скрипта: 0:00:03.39


$ python task_4_2b.py "sh clock" 192.168.100.1 192.168.100.2 192.168.100.3 -u cisco -p cisco -s cisco -t 1 --timed
['sh clock\r\n*08:32:01.886 UTC Fri Sep 11 2020\r\nR1#',
 'sh clock\r\n*08:32:02.947 UTC Fri Sep 11 2020\r\nR2#',
 'sh clock\r\n*08:32:04.007 UTC Fri Sep 11 2020\r\nR3#']

Время выполнения скрипта: 0:00:03.39


$ python task_4_2b.py "sh clock" 192.168.100.1 192.168.100.2 192.168.100.3 -u cisco -p cisco -s cisco -t 3 --timed
['sh clock\r\n*08:32:10.437 UTC Fri Sep 11 2020\r\nR2#',
 'sh clock\r\n*08:32:10.581 UTC Fri Sep 11 2020\r\nR1#',
 'sh clock\r\n*08:32:10.624 UTC Fri Sep 11 2020\r\nR3#']

Время выполнения скрипта: 0:00:01.28

Для этого задания нет теста!
"""
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
import yaml
from task_4_2 import send_show_command, send_command_to_devices


# Это просто заготовка, чтобы не забыть, что click надо применять к этой функции
def cli():
    # pprint(send_command_to_devices(devices, command, threads))
    pass


if __name__ == "__main__":
    cli()
