from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat
import logging
import click

import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import SSHException

import logging
import sys
from logging_filters import MessageFilter


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

fmt = logging.Formatter(
    "{asctime} - {name} - {levelname} - {message}", style="{"
)

# Вывод на stderr
stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

log.addHandler(stderr)

# Вывод log в файл

lfile = logging.FileHandler("logfile.txt")
lfile.setLevel(logging.DEBUG)
lfile.setFormatter(fmt)
lfile.addFilter(MessageFilter("Received"))

log.addHandler(lfile)


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
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    send_command_to_devices(devices, "sh ip int br")
