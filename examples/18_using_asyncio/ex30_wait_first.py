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
                raise ValueError
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
        tasks, return_when=asyncio.FIRST_EXCEPTION
    )
    print(f"{done_set=}")
    print(f"{pending_set=}")
    results1 = await asyncio.gather(*done_set, return_exceptions=True)
    results2 = await asyncio.gather(*pending_set, return_exceptions=True)
    return results1, results2

if __name__ == "__main__":
    print(asyncio.run(run_all(devices, "sh clock")))
