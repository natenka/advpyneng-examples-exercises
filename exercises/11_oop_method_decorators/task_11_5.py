# -*- coding: utf-8 -*-
"""
Задание 11.5

В задании есть класс CiscoTelnet. Надо добавить этому классу альтернативный
конструктор CiscoTelnet.input_params, который запрашивает недостающие
параметры. Обязательные параметры для создания подключения: host, username, password.
Если одного из этих параметров нет, надо запросить его с помощью input (пароли
будет видно, но тут input делается для упрощения тестов).
Конструктор должен возвращать экземпляр класса CiscoTelnet.

Пример использования конструктора:
In [1]: from task_11_5 import CiscoTelnet

In [3]: r1_params = {
   ...:     "host": "192.168.100.1",
   ...:     "username": "cisco",
   ...: }

In [4]: r1 = CiscoTelnet.input_params(**r1_params)
Enter password: cisco

In [5]: r1.send_show_command("sh clock")
Out[5]: 'sh clock\n*09:56:47.563 UTC Tue Sep 21 2021\nR1>'

In [6]: r1 = CiscoTelnet.input_params(host="192.168.100.1")
Enter password: cisco
Enter username: cisco

In [7]: r1.send_show_command("sh clock")
Out[7]: 'sh clock\n*09:58:01.311 UTC Tue Sep 21 2021\nR1>'

Для выполнения задания можно менять класс CiscoTelnet, в том числе существующие
методы, но нельзя удалять методы.

Тест использует файл devices.yaml для проверки работы класса CiscoTelnet,
если у вас другие параметры подключения к оборудованию, надо изменить их
в devices.yaml. Для этого задания используется только первое устройство
в файле devices.yaml. У первого устройства обязательно должны быть указаны
все параметры из обязательных: host, username, password.
"""
import time
import telnetlib
from collections.abc import Iterable
import re


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
    }
    with CiscoTelnet(**r1_params) as r1:
        print(r1.send_show_command("sh clock"))
