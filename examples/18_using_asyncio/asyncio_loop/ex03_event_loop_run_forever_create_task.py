import asyncio
import time
from pprint import pprint

from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException

from devices_scrapli import devices


async def send_show(device, command):
    try:
        async with AsyncScrapli(**device) as conn:
            reply = await conn.send_command(command)
        return reply.result
    except ScrapliException as error:
        print(error)


async def run_all(devices, command):
    print("Running all...")
    coro = [send_show(dev, command) for dev in devices]
    result = await asyncio.gather(*coro, return_exceptions=True)
    print("All done")
    return result


if __name__ == "__main__":
    coro = run_all(devices, "sh clock")

    loop = asyncio.get_event_loop()
    task = loop.create_task(coro)
    print("Sleeping...")
    time.sleep(5)
    print(f"{loop.is_running()=}")
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
