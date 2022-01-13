# -*- coding: utf-8 -*-
"""
Задание 11.3

В задании есть класс CiscoTelnet. Надо добавить этому классу переменную
экземпляра - cfg, при обращении к которой будет считываться текущая
конфигурация с оборудования. Чтобы конфигурация не считывалась каждый раз
при обращении к переменной, надо реализовать кеширование конфига.

В методе __init__ надо добавить параметр config_cache_timeout, который
будет контролировать время хранения кеша. Значение по умолчанию 60 (секунд).

Например, при создании экземпляра класса CiscoTelnet, конфиг еще не считывался,
поэтому при обращении r1.cfg - не оборудовании выполняется команда sh run и
возвращается текущая конфигурация. Если после этого сразу поменять конфиг и
снова обратиться к r1.cfg, конфигурация еще старая, без новых изменений.
А если сделать паузу >= config_cache_timeout и повторить r1.cfg, конфиг уже
должен считываться заново и показывать внесенные изменения.

Пример работы с config_cache_timeout=4. Для упрощения вывода, команда sh run
временно заменена на sh run | i ^interface Loop, но для прохождения тестов
надо чтобы выполнялась именно sh run:

In [2]: r1_params = {
   ...:     "host": "192.168.100.1",
   ...:     "username": "cisco",
   ...:     "password": "cisco",
   ...:     "secret": "cisco",
   ...:     "config_cache_timeout": 4,
   ...: }

In [3]: from task_11_3 import CiscoTelnet

In [4]: r1 = CiscoTelnet(**r1_params)

In [11]: print(r1.cfg)
sh run | i ^interface Loop
interface Loopback100
interface Loopback200
R1#

In [12]: r1.send_config("interface loopback22")
    ...: print(r1.cfg)
sh run | i ^interface Loop
interface Loopback100
interface Loopback200
R1#

In [13]: time.sleep(5)
    ...: print(r1.cfg)
    ...:
sh run | i ^interface Loop
interface Loopback22
interface Loopback100
interface Loopback200
R1#

Для выполнения задания можно менять класс CiscoTelnet, в том числе существующие
методы, но нельзя удалять методы.

Тест использует файл devices.yaml для проверки работы класса CiscoTelnet,
если у вас другие параметры подключения к оборудованию, надо изменить их
в devices.yaml. Для этого задания используется только первое устройство
в файле devices.yaml.
"""
import time
import telnetlib
from collections.abc import Iterable
import re

import yaml


class CiscoTelnet:
    def __init__(
        self,
        host,
        username,
        password,
        secret=None,
        read_timeout=5,
        encoding="utf-8",
    ):
        self.host = host
        self.username = username
        self.prompt = ">"
        self.read_timeout = read_timeout
        self.encoding = encoding

        self._telnet = telnetlib.Telnet(host)
        self._read_until("Username")
        self._write_line(username)
        self._read_until("Password")
        self._write_line(password)

        match_index, match_obj, output = self._telnet.expect(
            [b">", b"#"], timeout=self.read_timeout
        )
        if not match_obj:
            raise ValueError("Cisco prompt not found")
        self.hostname = re.search(r"(\S+)[#>]", output.decode(self.encoding)).group(1)
        if match_index == 0 and secret:
            self._write_line("enable")
            self._read_until("Password")
            self._write_line(secret)
            self._read_until("#")
            self.prompt = "#"
        elif match_index == 1:
            self.prompt = "#"
        self._write_line("terminal length 0")
        self._read_until(self.prompt)

    def _read_until(self, line):
        output = self._telnet.read_until(
            line.encode(self.encoding), timeout=self.read_timeout
        )
        return output.decode(self.encoding).replace("\r\n", "\n")

    def _write_line(self, line):
        self._telnet.write(f"{line}\n".encode(self.encoding))

    def send_show_command(self, command):
        self._write_line(command)
        command_output = self._read_until(self.prompt)
        return command_output

    def send_config(self, commands):
        if isinstance(commands, str):
            commands = ["conf t", commands, "end"]
        elif isinstance(commands, Iterable):
            commands = ["conf t", *commands, "end"]
        else:
            raise ValueError("commands should be iterable")
        output = ""
        for cmd in commands:
            self._write_line(cmd)
            output += self._read_until(self.prompt)
        return output

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._telnet.close()


if __name__ == "__main__":
    r1_params = {
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
        "config_cache_timeout": 4,
    }
    # пример использования cfg, до выполнения задания будет ошибка
    with CiscoTelnet(**r1_params) as r1:
        print(r1.cfg)
        r1.send_config("interface loopback77")
        print(r1.cfg)
        time.sleep(5)
        print(r1.cfg)
