from base_class import BaseSSH
import time


class CiscoSSH(BaseSSH):
    def __init__(self, ip, username, password, enable_password, disable_paging=True):
        super().__init__(ip, username, password)
        self._ssh.send("enable\n")
        self._ssh.send(enable_password + "\n")
        if disable_paging:
            self._ssh.send("terminal length 0\n")
        time.sleep(1)
        self._ssh.recv(self._MAX_READ)
        self._cfg = None
        self._mgmt_ip = None

    def config_mode(self):
        self._ssh.send("conf t\n")
        time.sleep(0.5)
        result = self._ssh.recv(self._MAX_READ).decode("ascii")
        return result

    def exit_config_mode(self):
        self._ssh.send("end\n")
        time.sleep(0.5)
        result = self._ssh.recv(self._MAX_READ).decode("ascii")
        return result

    def send_config_commands(self, commands):
        result = self.config_mode()
        result += super().send_config_commands(commands)
        result += self.exit_config_mode()
        return result

    @property
    def cfg(self):
        if not self._cfg:
            self._cfg = self.send_show_command("sh run")
        return self._cfg

    @property
    def mgmt_ip(self):
        if not self._mgmt_ip:
            loopback0 = self.send_show_command("sh run interface lo0")
            self._mgmt_ip = re.search("ip address (\S+) ", loopback0).group(1)
        return self._mgmt_ip

    @mgmt_ip.setter
    def mgmt_ip(self, new_ip):
        if self.mgmt_ip != new_ip:
            self.send_config_commands(
                [f"interface lo0", f"ip address {new_ip} 255.255.255.255"]
            )
            self._mgmt_ip = new_ip

    @staticmethod
    def _parse_show(command, command_output, index_file="index", templates="templates"):
        attributes = {"Command": command, "Vendor": "cisco_ios"}
        cli_table = clitable.CliTable(index_file, templates)
        cli_table.ParseCmd(command_output, attributes)
        return [dict(zip(cli_table.header, row)) for row in cli_table]

    def send_show_command(self, command, parse=True):
        command_output = super().send_show_command(command)
        if not parse:
            return command_output
        return self._parse_show(command, command_output)  #
