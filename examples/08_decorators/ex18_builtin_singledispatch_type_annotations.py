from netmiko import ConnectHandler
import yaml
from pprint import pprint
from collections.abc import Iterable
from functools import singledispatch

@singledispatch
def send_commands(command, device):
    print("Все пропало")
    raise ValueError(f"Тип {type(command).__name__} не поддерживается")

@send_commands.register
def _(config_commands: Iterable, device):
    print("config")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result

@send_commands.register
def _(show_command: str, device):
    print("show")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show_command)
    return result


if __name__ == "__main__":
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    show_command = "sh ip int br"
    with open("devices.yaml") as f:
        dev_list = yaml.safe_load(f)
        r1 = dev_list[0]
    #send_commands(commands, r1)
    send_commands(show_command, r1)
    send_commands(tuple(commands), r1)
