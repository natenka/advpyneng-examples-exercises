import telnetlib
import time
import logging
import re
import os

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class CiscoTelnet:
    def __init__(
        self, ip, username, password, enable_password=None, disable_paging=True
    ):
        print("__init__")
        log.debug(f"Telnet подключение к {ip}")
        self.ip = ip
        self._mngmt_ip = None
        self._config = None
        self._telnet = telnetlib.Telnet(ip)
        self._telnet.read_until(b"Username:")
        self._telnet.write(username.encode("utf-8") + b"\n")

        self._telnet.read_until(b"Password:")
        self._telnet.write(password.encode("utf-8") + b"\n")
        if enable_password:
            self._telnet.write(b"enable\n")
            self._telnet.read_until(b"Password:")
            self._telnet.write(enable_password.encode("utf-8") + b"\n")
        if disable_paging:
            self._telnet.write(b"terminal length 0\n")
        time.sleep(1)
        self._telnet.read_very_eager()

    @classmethod
    def from_prompt(cls, ip):
        params = {"ip": ip}
        for p in ("username", "password"):
            params[p] = input(f"{p.upper()}: ")
        return cls(**params)

    @classmethod
    def from_envvars(cls, prefix="CISCO_"):
        for p in ("ip", "username", "password"):
            params[p] = os.envvar.get(prefix + p)
        return cls(**params)

    def __repr__(self):
        return f"<CiscoTelnet ip={self.ip}>"

    @staticmethod
    def _parse_show(
        command, command_output, index_file='index', templates='templates'
    ):
        attributes = {'Command': command}
        cli_table = clitable.CliTable(index_file, templates)
        cli_table.ParseCmd(command_output, attributes)
        return [dict(zip(cli_table.header, row)) for row in cli_table]


    def send_show_command(self, command):
        log.debug(f"Отправка команды {command} на {self.ip}")
        self._telnet.write(command.encode("utf-8") + b"\n")
        output = self._telnet.read_until(b"#").decode("utf-8")
        time.sleep(5)
        return output

    def send_config_commands(self, commands):
        log.debug(f"Отправка команд {commands} на {self.ip}")
        if type(commands) == str:
            commands = [commands]
        output = ""
        commands = ["conf t", *commands, "end"]
        for command in commands:
            self._telnet.write(command.encode("utf-8") + b"\n")
            output += self._telnet.read_until(b"#").decode("utf-8")
        return output


    def close(self):
        self._telnet.close()

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self._telnet.close()


