from base_ssh_class import BaseSSH
import time


class ErrorInCommand(Exception):
    pass


class CiscoSSH(BaseSSH):
    def __init__(
        self, ip, username, password, secret=None, disable_paging=True
    ):
        super().__init__(ip, username, password)
        if secret:
            self._ssh.send("enable\n")
            self._ssh.send(f"{secret}\n")
        if disable_paging:
            self._ssh.send("terminal length 0\n")
        time.sleep(1)
        self._ssh.recv(self._MAX_READ)

    @staticmethod
    def check_errors(output):
        if "Invalid" in output:
            raise ErrorInCommand("Возникла ошибка при выполнении команды")

    def send_show_command(self, command):
        output = super().send_show_command(command)
        self.check_errors(output)
        return output

    def config_mode(self):
        self._ssh.send("conf t\n")
        time.sleep(0.5)
        output = self._ssh.recv(self._MAX_READ).decode("utf-8")
        return output

    def exit_config_mode(self):
        self._ssh.send("end\n")
        time.sleep(0.5)
        output = self._ssh.recv(self._MAX_READ).decode("utf-8")
        return output

    def send_config_commands(self, commands):
        output = self.config_mode()
        output += super().send_config_commands(commands)
        output += self.exit_config_mode()
        return output


