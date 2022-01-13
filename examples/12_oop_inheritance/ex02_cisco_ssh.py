import time
from base_ssh_class import BaseSSH
from ex11_mixin_pprint import PprintMixin

class CiscoSSH(PprintMixin, BaseSSH):
    def __init__(self, ip, username, password, secret=None):
        super().__init__(ip, username, password)
        print("__init__", self.ip)
        self.send_show_command("terminal length 0")
        if secret:
            self._ssh.send("enable\n")
            time.sleep(0.2)
            self._ssh.send(f"{secret}\n")
        time.sleep(1)
        self._ssh.recv(self._MAX_READ)

    def send_config_commands(self, commands):
        if isinstance(commands, str):
            commands = [commands]
        commands = ["conf t", *commands, "end"]
        result = super().send_config_commands(commands)
        return result


if __name__ == "__main__":
    r1 = CiscoSSH("192.168.100.1", "cisco", "cisco", "cisco")
    r1.pprint(methods=True)
