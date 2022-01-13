import telnetlib
import time
import logging
import re

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class CiscoTelnet:
    def __init__(
        self, ip, username, password, enable_password=None, disable_paging=True
    ):
        print("__init__")
        log.debug(f"Telnet подключение к {ip}")
        self.ip = ip
        self._config = None
        self._mngmt_ip = None
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

    def __repr__(self):
        return f"<CiscoTelnet ip={self.ip}>"

    def clear_cache(self):
        self._config = None

    @property
    def config(self):
        if self._config is None:
            self._config = self.send_show_command("sh run | i hostname")
        return self._config

    @property
    def mngmt_ip(self):
        if self._mngmt_ip is None:
            output = self.send_show_command("sh run int Loopback 0")
            match = re.search("ip address (\S+)", output)
            if match:
                self._mngmt_ip = match.group(1)
        return self._mngmt_ip

    @mngmt_ip.setter
    def mngmt_ip(self, new_ip):
        if new_ip != self._mngmt_ip:
            self.send_config_commands(
                ["interface loop0", f"ip address {new_ip} 255.255.255.255"]
            )
            self._mngmt_ip = new_ip

    def send_show_command(self, command):
        log.debug(f"Отправка команды {command} на {self.ip}")
        self._telnet.write(command.encode("utf-8") + b"\n")
        output = self._telnet.read_until(b"#").decode("utf-8")
        time.sleep(3)
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

