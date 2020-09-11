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


async def send_command_to_devices(devices, command):
    try:
        coroutines = map(connect_ssh, devices, repeat(command))
        result = await asyncio.gather(*coroutines)
        return result
    except asyncio.CancelledError as e:
        print("Отмена операции")


def main():
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)

    loop = asyncio.get_event_loop()
    coroutine = send_command_to_devices(devices, "sh clock")
    try:
        result = loop.run_until_complete(coroutine)
    except KeyboardInterrupt:
        print("Starting shutdown")
    finally:
        tasks = asyncio.Task.all_tasks()
        for t in tasks:
            t.cancel()
        data = loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
        print(data)
    loop.close()


if __name__ == "__main__":
    main()
