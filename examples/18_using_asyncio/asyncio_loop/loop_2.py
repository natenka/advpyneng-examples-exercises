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
    except asyncio.CancelledError:
        await asyncio.sleep(5)
        print(f'### Отменено подключение к {device["host"]}')


async def send_command_to_devices(devices, command):
    try:
        tasks = []
        for device in devices:
            task = asyncio.create_task(connect_ssh(device, command))
            tasks.append(task)
        result = await asyncio.gather(*tasks, return_exceptions=True)
        return result
    except asyncio.CancelledError:
        print(f'### Отменена send_command_to_devices')


async def shutdown():
    tasks = [task for task in asyncio.all_tasks()
             if task is not asyncio.current_task()]
    for task in tasks:
        task.cancel()
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results


if __name__ == "__main__":
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    coro = send_command_to_devices(devices, "sh clock")

    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(coro)
    except KeyboardInterrupt:
        print("Отмена задач")
        results = loop.run_until_complete(shutdown())
        print(results)
    loop.close()
