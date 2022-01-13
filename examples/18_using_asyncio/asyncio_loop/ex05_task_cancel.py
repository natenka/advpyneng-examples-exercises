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
            await asyncio.sleep(5)
            print(f'<<< Получен результат от {host}')
        return reply.result
    except ScrapliException as error:
        print(error)
    except asyncio.CancelledError:
        print(f'### Отменено подключение к {host}')


async def run_all(devices, command):
    try:
        tasks = [asyncio.create_task(send_show(dev, command)) for dev in devices]
        result = await asyncio.gather(*tasks, return_exceptions=True)
        return result
    except asyncio.CancelledError:
        print(f'### Отменена send_command_to_devices')


async def main():
    task = asyncio.create_task(run_all(devices, "sh clock"))
    await asyncio.sleep(2)
    task.cancel()
    await task


if __name__ == "__main__":
    coro = main()

    loop = asyncio.get_event_loop()
    # loop.set_debug(True)
    result = loop.run_until_complete(coro)
    loop.close()
