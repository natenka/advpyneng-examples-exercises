from pprint import pprint
import asyncio
from itertools import repeat
from random import random

import yaml
import netdev


async def connect_ssh(device, command):
    print(f'>>> Подключаюсь к {device["host"]}')
    try:
        async with netdev.create(**device) as ssh:
            await asyncio.sleep(random() * 10)
            output = await ssh.send_command(command)
            print(f'<<< Получен результат от {device["host"]}')
        return output
    except asyncio.CancelledError as e:
        print(f'Отмена операции {device["host"]}')


async def send_command_to_devices(devices, command, workers=2):
    semaphore = asyncio.Semaphore(workers)
    try:
        coroutines = [
            connect_ssh_with_semaphore(semaphore, device, command) for device in devices
        ]
        result = await asyncio.gather(*coroutines)
        return result
    except asyncio.CancelledError as e:
        print("Отмена операции")


async def connect_ssh_with_semaphore(semaphore, *args, **kwargs):
    async with semaphore:
        return await connect_ssh(*args, **kwargs)


def main():
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    asyncio.run(send_command_to_devices(devices, "sh clock"))


if __name__ == "__main__":
    main()
