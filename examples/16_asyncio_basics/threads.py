import time
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor, as_completed
import netmiko
import yaml
import random


def send_show(device, show):
    sl = random.random() * 10
    print(f"{device['host']} спит {sl}")
    time.sleep(sl)
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show)
        return device['host'], result


with open('devices.yaml') as f:
    devices = yaml.safe_load(f)


