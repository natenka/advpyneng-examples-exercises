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


async def connect_ssh(device, command, semaphore):
    async with semaphore:
        print(f'ASYNC Подключаюсь к {device["host"]}')
        async with netdev.create(**device) as ssh:
            output = await ssh.send_command(command)
            print(f'ASYNC Получен результат от {device["host"]}')
        return output


async def send_command_to_devices(devices, command):
    executor = ThreadPoolExecutor(max_workers=2)
    semaphore = asyncio.Semaphore(1)
    tasks = []
    for device in devices:
        if device["host"] in sync_only:
            loop = asyncio.get_running_loop()
            tasks.append(
                loop.run_in_executor(executor, connect_ssh_netmiko, device, command)
            )
        else:
            tasks.append(asyncio.create_task(connect_ssh(device, command, semaphore)))
    result = await asyncio.gather(*tasks)
    return result


if __name__ == "__main__":
    sync_only = ["192.168.100.2"]
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(send_command_to_devices(devices, "sh run | i hostname"))
    print(result)
