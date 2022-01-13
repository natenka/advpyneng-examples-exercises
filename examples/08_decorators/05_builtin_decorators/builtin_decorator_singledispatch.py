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


@send_commands.register(str)
def _(command, device):
    print("str")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


@send_commands.register(Iterable)
def _(config_commands, device):
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
