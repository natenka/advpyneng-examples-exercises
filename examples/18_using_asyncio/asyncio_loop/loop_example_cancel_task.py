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
        tasks = []
        for device in devices:
            task = asyncio.create_task(connect_ssh(device, command))
            task.set_name(device["host"])
            tasks.append(task)
        result = await asyncio.gather(*tasks, return_exceptions=True)
        return result
    except asyncio.CancelledError as e:
        print("Отмена операции")


async def shutdown():
    await asyncio.sleep(30)
    tasks = [t for t in asyncio.Task.all_tasks() if t is not asyncio.current_task()]

    [t.cancel() for t in tasks]
    data = await asyncio.gather(*tasks, return_exceptions=True)
    return data


async def cancel_task_by_name(name):
    print("cancel_task_by_name")
    tasks = [t for t in asyncio.Task.all_tasks() if t.get_name() == name]

    [t.cancel() for t in tasks]
    data = await asyncio.gather(*tasks, return_exceptions=True)
    return data


def main():
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)

    loop = asyncio.get_event_loop()
    coroutine = send_command_to_devices(devices, "sh clock")
    try:
        result = loop.run_until_complete(coroutine)
    except KeyboardInterrupt:
        print("Starting shutdown")
        result = loop.run_until_complete(cancel_task_by_name("192.168.100.2"))
    finally:
        result = loop.run_until_complete(shutdown())
        print(result)
    loop.close()


if __name__ == "__main__":
    main()
