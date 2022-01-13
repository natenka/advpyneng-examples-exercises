from abc_base_ssh_class import BaseSSH
import time


class ErrorInCommand(Exception):
    pass


class CiscoSSH(BaseSSH):
    def __init__(self, ip, username, password, enable, disable_paging=True):
        super().__init__(ip, username, password)
        self._ssh.send("enable\n")
        self._ssh.send(f"{enable}\n")
        if disable_paging:
            self._ssh.send("terminal length 0\n")
        time.sleep(1)
        self._ssh.recv(self._MAX_READ)

    def send_config_commands(self, commands):
        super().send_config_commands(commands)

    def send_show_command(self, command):
        super().send_show_command()
