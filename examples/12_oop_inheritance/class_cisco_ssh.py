from base_ssh_class import BaseSSH
import time
from mixin_code import SourceCodeMixin


class ErrorInCommand(Exception):
    pass


class CiscoSSH(BaseSSH, SourceCodeMixin):
    def __init__(self, ip, username, password, enable, disable_paging=True):
        super().__init__(ip, username, password)
        self._ssh.send("enable\n")
        self._ssh.send(f"{enable}\n")
        if disable_paging:
            self._ssh.send("terminal length 0\n")
        time.sleep(1)
        self._ssh.recv(self._MAX_READ)

    def send_config_commands(self, commands):
        self._ssh.send("conf t\n")
        output = super().send_config_commands(commands)
        self._ssh.send("end\n")
        time.sleep(1)
        output += self._ssh.recv(self._MAX_READ).decode("ascii")
        if "Invalid input" in output:
            raise ErrorInCommand("Возникла ошибка")
        return output
