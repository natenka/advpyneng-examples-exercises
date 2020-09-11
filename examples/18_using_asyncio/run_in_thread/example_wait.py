from pprint import pprint
import asyncio
from itertools import repeat

import yaml
import netdev
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
import time


async def connect_ssh(device, command):
    print(f'ASYNC Подключаюсь к {device["host"]}')
    async with netdev.create(**device) as ssh:
        output = await ssh.send_command(command)
        await asyncio.sleep(5)
    print(f'ASYNC Получен результат от {device["host"]}')
    return output


async def send_command_to_devices(devices, command):
    tasks = []
    for device in devices:
        tasks.append(asyncio.create_task(connect_ssh(device, command)))
    done, pending = await asyncio.wait(tasks, timeout=10)
    # result = [t.result() for t in success]
    print(done, pending)
    # result = await asyncio.gather(pending)
    return done, pending


if __name__ == "__main__":
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(send_command_to_devices(devices, "sh run | i hostname"))
    print("#" * 100)
    print(result)
