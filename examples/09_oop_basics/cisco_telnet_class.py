import telnetlib
import time


import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class CiscoTelnet:
    def __init__(
        self, ip, username, password, enable_password=None, disable_paging=True
    ):
        print("__init__")
        log.debug(f"Telnet подключение к {ip}")
        self.ip = ip
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

    def send_show_command(self, command):
        log.debug(f"Отправка команды {command} на {self.ip}")
        self._telnet.write(command.encode("utf-8") + b"\n")
        output = self._telnet.read_until(b"#").decode("utf-8")
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


if __name__ == "__main__":
    with CiscoTelnet("192.168.100.1", "cisco", "cisco", "cisco") as r1:
        print(r1.send_show_command("sh clock"))
        raise IndexError
