from pprint import pprint
import time
import yaml
from itertools import repeat
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor


def connect_ssh(device, command):
    # print(f'Подключаюсь к {device["host"]}')
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_devices(devices, command):
    with ThreadPoolExecutor(max_workers=30) as executor:
        result = list(executor.map(connect_ssh, devices, repeat(command)))
    return result


if __name__ == "__main__":
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    result = send_command_to_devices(devices, "sh run")
    print(len(result))
    # pprint(list(map(len, result)))
    # with open('testfile_sh_run_all_netmiko.txt', 'w') as f:
    #    f.write(result[0])
