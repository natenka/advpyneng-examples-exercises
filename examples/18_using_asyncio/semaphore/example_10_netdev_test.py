from pprint import pprint
import asyncio
from itertools import repeat

import yaml
import netdev


async def connect_ssh(semaphore, device, command):
    async with semaphore:
        print(f'Подключаюсь к {device["host"]}')
        async with netdev.create(**device) as ssh:
            output = await ssh.send_command(command)
            await asyncio.sleep(2)
        print(f'Получен результат от {device["host"]}')
        return output


async def connect_ssh_workers(semaphore, *args, **kwargs):
    async with semaphore:
        return await connect_ssh(*args, **kwargs)


async def send_command_to_devices(devices, command, max_workers=1):
    semaphore = asyncio.Semaphore(max_workers)
    coroutines = [connect_ssh(semaphore, device, command) for device in devices]
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(send_command_to_devices(devices, "sh run", max_workers=10))
