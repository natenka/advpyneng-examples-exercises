from functools import singledispatch
from netmiko import ConnectHandler
import yaml
from pprint import pprint
from collections.abc import Iterable


@singledispatch
def send_commands(command, device):
    print("singledispatch")
    raise NotImplementedError("Поддерживается только строка или iterable")


# send_commands = singledispatch(send_commands)


@send_commands.register
def _(show_command: str, device):
    print("Аргумент строка")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show_command)
    return result


@send_commands.register
def _(config_commands: Iterable, device):
    print("Аргумент iterable")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result


if __name__ == "__main__":
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    show_command = "sh ip int br"
    r1 = {
        "device_type": "cisco_ios",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
        "ip": "192.168.100.1",
    }
    send_commands(tuple(commands), r1)
    send_commands(show_command, r1)
