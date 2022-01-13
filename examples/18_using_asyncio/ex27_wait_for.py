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
            await asyncio.sleep(1)
        return reply.result
    except ScrapliException as error:
        print(error, host)
    except asyncio.CancelledError:
        print(f"Отмена... {host}")
        await asyncio.sleep(2)
        print("Отменено")


async def run_all(devices, command):
    try:
        coro = [send_show(dev, command) for dev in devices]
        result = await asyncio.gather(*coro, return_exceptions=True)
        return result
    except asyncio.CancelledError:
        print(f"Отмена run all...")


async def main():
    task = asyncio.create_task(run_all(devices, "sh clock"))
    # await asyncio.sleep(1)
    # task.cancel()
    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=1)
    except asyncio.TimeoutError as error:
        print(f"{error=}")
    answer = input(
        "Задача выполняется слишком долго. Продолжать выполнение? "
    )
    if answer == "y":
        await task
    else:
        task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
