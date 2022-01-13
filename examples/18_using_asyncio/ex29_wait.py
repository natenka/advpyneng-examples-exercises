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
                await asyncio.sleep(5)
        return host, reply.result
    except ScrapliException as error:
        print(error, host)
    except asyncio.CancelledError:
        print(f"Отмена... {host}")
        await asyncio.sleep(2)
        print("Отменено")


async def run_all(devices, command):
    tasks = [
        asyncio.create_task(send_show(dev, command)) for dev in devices
    ]
    done_set, pending_set = await asyncio.wait(
        tasks, timeout=5, return_when=asyncio.ALL_COMPLETED
    )
    print(f"{done_set=}")
    print(f"{pending_set=}")
    [t.cancel() for t in pending_set]
    #results = [await t for t in done_set]
    results = [await t for t in tasks if t not in pending_set]
    return results

if __name__ == "__main__":
    print(asyncio.run(run_all(devices, "sh clock")))
