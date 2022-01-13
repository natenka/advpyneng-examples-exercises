import asyncio
import yaml
from pprint import pprint
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
from devices_scrapli import devices


async def send_show(device, command):
    host = device["host"]
    print(f"Подключаюсь к {host}")
    try:
        async with AsyncScrapli(**device) as conn:
            reply = await conn.send_command(command)
            if host == "192.168.100.1":
                await asyncio.sleep(10)
            print(f"Получен результат от {host}")
        return reply.result
    except ScrapliException as error:
        print(error)
    except asyncio.CancelledError:
        print("Отмена...")
        await asyncio.sleep(10)
        print("Отменено")


async def run_all(devices, command):
    try:
        coro = [send_show(dev, command) for dev in devices]
        result = await asyncio.gather(*coro, return_exceptions=True)
        return result
    except asyncio.CancelledError:
        print("Отмена run_all")


if __name__ == "__main__":
    output = asyncio.run(run_all(devices, "sh clock"))
    pprint(output)
