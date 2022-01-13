from netmiko import ConnectHandler
import yaml
from pprint import pprint


def send_show_command(device, show_command):
    print("show")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show_command)
    return result


def send_config_commands(device, config_commands):
    print("config")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result


def send_commands(device, command):
    if type(command) == str:
        return send_show_command(device, command)
    elif type(command) == list:
        return send_config_commands(device, command)


if __name__ == "__main__":
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    show_command = "sh ip int br"
    with open("devices.yaml") as f:
        dev_list = yaml.safe_load(f)

    send_commands(dev_list[0], commands)
    send_commands(dev_list[0], show_command)
