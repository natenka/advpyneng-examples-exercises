from concurrent.futures import ThreadPoolExecutor
import sys
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat
import logging
import click

import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import SSHException
from rich.logging import RichHandler

fmt = logging.Formatter(
    "{threadName} {funcName} {name} {levelname} {message}",
    style="{"
)
stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

logfile = logging.FileHandler("logfile.log")
logfile.setLevel(logging.DEBUG)
logfile.setFormatter(fmt)

# logger
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(stderr)
log.addHandler(logfile)

# netmiko logger
logf = logging.FileHandler("miko.log")
logf.setLevel(logging.DEBUG)
logf.setFormatter(fmt)

netmiko = logging.getLogger("netmiko")
netmiko.setLevel(logging.DEBUG)
netmiko.addHandler(logf)

miko = logging.getLogger("paramiko")
miko.setLevel(logging.DEBUG)
miko.addHandler(logf)


def send_show(device_dict, command):
    ip = device_dict["host"]
    log.info(f"===>  Connection: {ip}")

    try:
        with ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            log.debug(f"<===  Received:   {ip}")
            log.debug(f"Получен вывод команды {command} с {ip}")
        return result
    except SSHException as error:
        #log.exception(f"Ошибка {error} на {ip}")
        log.error(f"Ошибка {error} на {ip}")


def send_command_to_devices(devices, command):
    log.debug("START")
    data = {}
    with ThreadPoolExecutor(max_workers=2) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for device, output in zip(devices, result):
            data[device["host"]] = output
    return data


if __name__ == "__main__":
    click.clear()
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    send_command_to_devices(devices, "sh ip int br")
