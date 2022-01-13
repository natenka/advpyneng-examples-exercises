from pprint import pprint
import asyncio
from itertools import repeat

import yaml
import netdev
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
import time


def connect_ssh_netmiko(device, command):
    print(f'SYNC Подключаюсь к {device["host"]}')
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        time.sleep(2)
        print(f'SYNC Получен результат от {device["host"]}')
    return result


async def connect_ssh(device, command):
    print(f'ASYNC Подключаюсь к {device["host"]}')
    async with netdev.create(**device) as ssh:
        output = await ssh.send_command(command)
        print(f'ASYNC Получен результат от {device["host"]}')
    return output


async def send_command_to_devices(devices, command):
    loop = asyncio.get_running_loop()
    executor = ThreadPoolExecutor(max_workers=10)
    tasks = []
    for device in devices:
        if device["host"] in netmiko_only:
            task = loop.run_in_executor(
                executor, connect_ssh_netmiko, device, command
            )
            tasks.append(task)
        else:
            task = asyncio.create_task(connect_ssh(device, command))
            tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


if __name__ == "__main__":
    netmiko_only = ["192.168.100.2"]
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)

    results = asyncio.run(send_command_to_devices(devices, "sh clock"))
    print(results)
