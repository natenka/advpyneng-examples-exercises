from pprint import pprint
import asyncio
from itertools import repeat

import yaml
import netdev
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import logging

logger = logging.getLogger("My Script")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(
    logging.Formatter(
        "%(asctime)s - THREAD %(thread)d - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
)

logger.addHandler(console)


start_msg = "===> Connection to: {}, function {}"
received_msg = "<=== Result from: {}, function {}"


def connect_ssh_sync(device, command, name):
    logger.info(start_msg.format(device["host"], name))
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        logger.info(received_msg.format(device["host"], name))
    return result


async def send_command_to_devices(devices, command, name, executor=None):
    tasks = []
    for device in devices:
        loop = asyncio.get_running_loop()
        tasks.append(
            loop.run_in_executor(executor, connect_ssh_sync, device, command, name)
        )
    result = await asyncio.gather(*tasks)
    return result


async def main():
    coro1 = send_command_to_devices(devices, "sh run | i hostname", "RUN1")
    coro2 = send_command_to_devices(devices, "sh run | i ospf", "RUN2")
    result = await asyncio.gather(coro1, coro2)
    pprint(result)


if __name__ == "__main__":
    sync_only_devices = ["192.168.100.2"]
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(main())
