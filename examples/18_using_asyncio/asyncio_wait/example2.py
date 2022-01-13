from pprint import pprint
import asyncio
from itertools import repeat
import random
import yaml
import netdev
from datetime import datetime


async def connect_ssh(device, command):
    print(f'Подключаюсь к {device["host"]}')
    async with netdev.create(**device) as ssh:
        output = await ssh.send_command(command)
        sl = random.choice([3, 8, 2, 1, 7])
        print(f'Спим {sl} {device["host"]}')
        await asyncio.sleep(sl)
    print(f'Получен результат от {device["host"]}')
    return output


async def send_command_to_devices(devices, command, max_time=8):
    cancelled = []
    tasks = [asyncio.create_task(connect_ssh(device, command))
             for device in devices]
    done, pending = await asyncio.wait(tasks, timeout=max_time)
    if pending:
        print(f"После {max_time} остались такие задачи")
        pprint(pending)
        answer = input("Отменить оставшиеся задачи [y/n]?: ")
        if answer.lower() in ("y", "yes"):
            for t in pending:
                t.cancel()
            cancelled = await asyncio.gather(*pending, return_exceptions=True)
            return done, cancelled
        else:
            results = await asyncio.gather(*pending, return_exceptions=True)
            return list(done) + results


if __name__ == "__main__":
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(send_command_to_devices(devices, "sh run"))
