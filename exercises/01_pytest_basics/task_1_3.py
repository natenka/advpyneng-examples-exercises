# -*- coding: utf-8 -*-
"""
Задание 1.3

Написать тесты для функции send_show. Тесты должны проверять:

* тип возвращаемых данных - словарь или None, если было исключение
* при возникновении исключения, опционально можно сделать проверку на то правильное ли
  выводится сообщение на stdout, как минимум, что в stdout был вывод IP-адреса
* что функция возвращает правильный результат при передаче команды строки
  и при передаче списка команд. И в том и в том случае должен возвращаться
  словарь в котором ключ команда, а значение вывод команды


Для проверки разных ситуаций - доступное устройство, недоступное и так далее
в файле devices.yaml создано несколько групп устройств:
* reachable_ssh_telnet - это устройства на которых доступен Telnet и SSH, прописаны
  правильные логин и пароли
* reachable_ssh_telnet_wrong_auth_password - это доступное устройство на котором разрешены
  SSH/Telnet, но настроен неправильный пароль auth_password
* reachable_telnet_only - это доступное устройство на котором разрешен только Telnet
  и прописаны правильные логин и пароли
* unreachable - это недоступное устройство

Для корректной работы тестов надо написать в файле devices.yaml параметры ваших устройств
или создать аналогичный файл с другим именем.
Плюс надо соответственно настроить устройства так чтобы где нужно был только
Telnet или неправильный пароль соответственно.

В целом тут свобода творчества и один из нюансов задания как раз в том чтобы
придумать что именно и как тестировать. В задании даны несколько идей для старта,
но остальное надо продумать самостоятельно.

Тест(ы) написать в файле заданий.

Ограничение: функцию менять нельзя.
Для заданий этого раздела нет тестов для проверки тестов :)
"""
import socket
from pprint import pprint

import yaml
from scrapli import Scrapli
from scrapli.exceptions import ScrapliException
from paramiko.ssh_exception import SSHException


def send_show(device, show_commands):
    transport = device.get("transport") or "system"
    host = device.get("host")
    if type(show_commands) == str:
        show_commands = [show_commands]
    cmd_dict = {}
    print(f">>> Connecting to {host}")
    try:
        with Scrapli(**device) as ssh:
            for cmd in show_commands:
                reply = ssh.send_command(cmd)
                cmd_dict[cmd] = reply.result
        print(f"<<< Received output from {host}")
        return cmd_dict
    except (ScrapliException, SSHException, socket.timeout, OSError) as error:
        print(f"Device {host}, Transport {transport}, Error {error}")


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev_type, device_list in devices.items():
        print(dev_type.upper())
        for dev in device_list:
            output = send_show(dev, "sh clock")
            pprint(output, width=120)
