from pprint import pprint
import asyncio
from itertools import repeat
from random import random

from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
from devices_scrapli import devices


async def send_show(device, command):
    try:
        host = device["host"]
        print(f'>>> Подключаюсь к {host}')
        async with AsyncScrapli(**device) as conn:
            reply = await conn.send_command(command)
            print(f'<<< Получен результат от {host}')
        return reply.result
    except ScrapliException as error:
        print(error)
    except asyncio.CancelledError:
        await asyncio.sleep(5)
        print(f'### Отменено подключение к {host}')


async def run_all(devices, command):
    try:
        coro = [send_show(dev, command) for dev in devices]
        # tasks = [asyncio.create_task(send_show(dev, command)) for dev in devices]
        result = await asyncio.gather(*coro, return_exceptions=True)
        return result
    except asyncio.CancelledError:
        print(f'### Отменена send_command_to_devices')


async def shutdown():
    tasks = [task for task in asyncio.all_tasks()
             if task is not asyncio.current_task()]
    # pprint(tasks)
    for task in tasks:
        task.cancel()
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results


if __name__ == "__main__":
    coro = run_all(devices, "sh clock")

    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(coro)
    except KeyboardInterrupt:
        print("Отмена задач")
        results = loop.run_until_complete(shutdown())
        print(results)
    loop.close()
