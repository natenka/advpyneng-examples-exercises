from pprint import pprint
import asyncio
from itertools import repeat

import yaml
import netdev


async def connect_ssh(device, command, semaphore):
    async with semaphore:
        print(f'Подключаюсь к {device["host"]}')
        async with netdev.create(**device) as ssh:
            output = await ssh.send_command(command)
        print(f'Получен результат от {device["host"]}')
        return output


async def func(semaphore):
    async with semaphore:
        print('>>>')
        await asyncio.sleep(0.5)
        print('<<<')

async def send_command_to_devices(devices, command, max_workers=1):
    sem = asyncio.Semaphore(5)
    coroutines = [connect_ssh(device, command, sem) for device in devices]
    sem2 = asyncio.Semaphore(5)
    coroutines2 = [func(sem2) for _ in range(10)]
    result = await asyncio.gather(*coroutines+coroutines2)
    return result


if __name__ == "__main__":
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(send_command_to_devices(devices, "sh run", max_workers=10))
