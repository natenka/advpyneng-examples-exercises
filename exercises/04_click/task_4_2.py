# -*- coding: utf-8 -*-
"""
Задание 4.2

Создать интерфейс командной строки для скрипта:

* аргумент command - команда которую надо отправить на оборудование
* опция --yaml-params, с коротким вариантом -y - YAML файл с параметрами подключения к оборудованию (devices.yaml). Тип click.File
* опция --threads, с коротким вариантом -t - количество потоков. Значение по умолчанию - 5, диапазон возможных значений 1-10.

Применить декораторы к функции cli!

В функции cli должна вызываться функция send_command_to_devices с правильными аргументами:
список словарей с параметрами подключения к устройствам, команда, кол-во потоков.
Значения аргументов для функции send_command_to_devices должны быть получены из
аргументов скрипта (из click).

Help скрипта:

$ python task_4_2.py --help
Usage: task_4_2.py [OPTIONS] COMMAND

Options:
  -y, --yaml-params FILENAME   [required]
  -t, --threads INTEGER RANGE  [default: 5]
  --help                       Show this message and exit.

Примеры использования скрипта:

$ python task_4_2.py "sh ip int br" -y devices.yaml
$ python task_4_2.py "sh ip int br" -y devices.yaml -t 1

$ python task_4_2.py "sh ip int br" -y devices.yaml -t 20
Usage: task_4_2.py [OPTIONS] COMMAND
Try 'task_4_2.py --help' for help.

Error: Invalid value for '--threads' / '-t': 20 is not in the valid range of 1 to 10.


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


def send_command_to_devices(devices, command, threads):
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
    # devices = yaml.safe_load(yaml_params)
    # pprint(send_command_to_devices(devices, command, threads), width=120)
    pass


if __name__ == "__main__":
    cli()
