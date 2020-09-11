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


# netmiko logger
net = logging.getLogger("netmiko")
net.setLevel(logging.DEBUG)
std = logging.StreamHandler()
std.setLevel(logging.DEBUG)

formatter = logging.Formatter("################ %(name)s %(levelname)s: %(message)s")
std.setFormatter(formatter)

net.addHandler(std)

#################

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

########## STDERR
stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(threadName)s %(name)s %(levelname)s: %(message)s")
stderr.setFormatter(formatter)

log.addHandler(stderr)


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
        log.exception("Ошибка")


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
    pprint(send_command_to_devices(devices, "sh clock"), width=120)
