# -*- coding: utf-8 -*-
"""
Задание 4.3

Создать интерфейс командной строки для скрипта по выводу help ниже.

Help скрипта:

$ python task_4_3.py --help
Usage: task_4_3.py [OPTIONS] COMMAND [ARGS]...

  Скрипт работает с устройствами в файле YAML_PARAMS и выполняет операции в
  потоках THREADS

Options:
  -y, --yaml-params FILENAME   [default: devices_task_4_3.yaml]
  -t, --threads INTEGER RANGE  [default: 5]
  --help                       Show this message and exit.

Commands:
  config  Отправить конфигурационные команды из файла COMMANDS
  ping    Пинг устройств из файла YAML_PARAMS
  show    Отправить show COMMAND и опционально парсить (PARSE) ее с помощью...

Help команд:

$ python task_4_3.py config --help
Usage: task_4_3.py config [OPTIONS] COMMANDS

  Отправить конфигурационные команды из файла COMMANDS

Options:
  --help  Show this message and exit.


$ python task_4_3.py ping --help
Usage: task_4_3.py ping [OPTIONS]

  Пинг устройств из файла YAML_PARAMS

Options:
  --help  Show this message and exit.


$ python task_4_3.py show --help
Usage: task_4_3.py show [OPTIONS] COMMAND

  Отправить show COMMAND и опционально парсить (PARSE) ее с помощью textfsm
  и/или записать результат в OUTPUT_FILE

Options:
  -o, --output-file FILENAME  Записать результат в файл
  -p, --parse                 Парсить вывод с помощью textfsm
  --help                      Show this message and exit.



Примеры использования скрипта (вывод сокращен):

Команда config отправляет команды из файла, который передается как аргумент на все указанные устройства:

$ python task_4_3.py -y devices_task_4_3.yaml config config_commands.txt
{'192.168.100.1': 'configure terminal\n'
                  'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                  'R1(config)#interface Loopback99\n'
                  'R1(config-if)#ip address 10.0.99.1 255.255.255.0\n'
                  'R1(config-if)#end\n'
                  'R1#',
 '192.168.100.2': 'configure terminal\n'
                  'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                  'R2(config)#interface Loopback99\n'
                  'R2(config-if)#ip address 10.0.99.1 255.255.255.0\n'
                  'R2(config-if)#end\n'
                  'R2#',
 '192.168.100.3': 'configure terminal\n'
                  'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                  'R3(config)#interface Loopback99\n'
                  'R3(config-if)#ip address 10.0.99.1 255.255.255.0\n'
                  'R3(config-if)#end\n'
                  'R3#'}

Команда ping пингует устройства из файла -y devices_task_4_3.yaml:

$ python task_4_3.py -y devices_task_4_3.yaml ping
Доступные адреса:   192.168.100.1, 192.168.100.2, 192.168.100.3
Недоступные адреса:

Команда show отправляет указанную команду show на все указанные устройства из файла -y devices_task_4_3.yaml и выводит результат:

$ python task_4_3.py -y devices_task_4_3.yaml show "sh clock"
{'192.168.100.1': '*09:22:19.639 UTC Mon Sep 21 2020',
 '192.168.100.2': '*09:22:19.656 UTC Mon Sep 21 2020',
 '192.168.100.3': '*09:22:19.783 UTC Mon Sep 21 2020'}

С опцией -p вывод команд парсится с помощью textfsm и выводится:

$ python task_4_3.py -y devices_task_4_3.yaml show "sh ip int br" -p
{'192.168.100.1': [{'interface': 'FastEthernet0/0',
                    'ip': '192.168.100.1',
                    'protocol': 'up',
                    'status': 'up'},
                   {'interface': 'Loopback99',
                    'ip': '10.0.99.1',
                    'protocol': 'up',
                    'status': 'up'}],
 '192.168.100.2': [{'interface': 'FastEthernet0/0',
                    'ip': '192.168.100.2',
                    'protocol': 'up',
                    'status': 'up'},
                   {'interface': 'Loopback99',
                    'ip': '10.0.99.1',
                    'protocol': 'up',
                    'status': 'up'}],
 '192.168.100.3': [{'interface': 'FastEthernet0/0',
                    'ip': '192.168.100.3',
                    'protocol': 'up',
                    'status': 'up'},
                   {'interface': 'Loopback99',
                    'ip': '10.0.99.1',
                    'protocol': 'up',
                    'status': 'up'}]}

Опция -o добавляет запись результата в файл (примеры файлов с записью данных выложены в каталоге 04_click):

$ python task_4_3.py -y devices_task_4_3.yaml show "sh ip int br" -p -o result.yaml
$ python task_4_3.py -y devices_task_4_3.yaml show "sh ip int br" -o result.txt""

"""
from concurrent.futures import ThreadPoolExecutor
import subprocess
from pprint import pprint
import yaml
from netmiko import ConnectHandler
from textfsm import clitable
import click


def ping_ip(ip):
    result = subprocess.run(["ping", "-c", "3", "-n", ip], stdout=subprocess.DEVNULL)
    ip_is_reachable = result.returncode == 0
    return ip_is_reachable


def ping_ip_addresses(ip_list, threads):
    reachable = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(ping_ip, ip_list)
    for ip, status in zip(ip_list, results):
        if status:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    return reachable, unreachable


def parse_command_dynamic(
    command_output, attributes_dict, index_file="index", templ_path="templates"
):

    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    return [dict(zip(cli_table.header, row)) for row in cli_table]


def send_cfg_commands(device, commands):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(commands)
    return result


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_devices(devices, threads, show=None, config=None):
    result_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for device in devices:
            if show:
                futures.append(executor.submit(send_show_command, device, show))
            elif config:
                futures.append(executor.submit(send_cfg_commands, device, config))
        for device, future in zip(devices, futures):
            result_dict[device["host"]] = future.result()
    return result_dict

