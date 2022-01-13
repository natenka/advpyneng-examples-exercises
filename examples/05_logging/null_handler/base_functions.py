import time
import logging
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

from netmiko import ConnectHandler
from netmiko.ssh_exception import SSHException

# Logging configuration
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def send_show(device_dict, command):
    ip = device_dict["host"]
    log.info(f"===>  Connection: {ip}")

    try:
        with ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            log.debug(f"<===  Received:   {ip}")
            log.debug(f"Получен вывод команды {command}\n\n{result}")
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
