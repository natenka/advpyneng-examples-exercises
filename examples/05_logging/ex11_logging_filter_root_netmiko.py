"""
filter for all loggers - apply to handler
https://stackoverflow.com/a/17276457/4527817
"""
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat
import logging
import yaml
from netmiko import (
    ConnectHandler,
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
)
from logging_filters import LevelFilter, MessageFilter


console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "{asctime} - {name} - {levelname} - {message}", datefmt="%H:%M:%S", style="{"
)
console.setFormatter(formatter)
console.addFilter(LevelFilter(logging.INFO))

# root logger + netmiko/paramiko
root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(console)

# script logger
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(console)


## messages
log.debug("Сообщение уровня debug")
log.debug("Сообщение уровня debug. test1")
log.debug("Сообщение уровня debug. test2")
log.info("Сообщение уровня info")
log.warning("Сообщение уровня warning")


def send_show(device_dict, command):
    ip = device_dict["host"]
    log.info(f"===> Connection: {ip}")  #
    try:
        with ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            log.debug(f"<=== Received:   {ip}")  ###
        return result
    except (NetMikoAuthenticationException, NetMikoTimeoutException) as err:
        log.warning(f"Ошибка при подключении {err}")


def send_command_to_devices(devices, command):
    log.debug(f"Подключаемся к {len(devices)} устройствам")  ###
    data = {}
    with ThreadPoolExecutor(max_workers=3) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for device, output in zip(devices, result):
            data[device["host"]] = output
    return data


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    print(send_command_to_devices(devices, "sh clock"))
