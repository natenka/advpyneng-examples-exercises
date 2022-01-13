import asyncio
import yaml
from pprint import pprint
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
from devices_scrapli import devices


async def send_show(device, command):
    try:
        async with AsyncScrapli(**device) as conn:
            reply = await conn.send_command(command)
            await asyncio.sleep(10)
        return reply.result
    except ScrapliException as error:
        print(error)
    except asyncio.CancelledError:
        print("Task is cancelled")
        raise


async def run_all(devices, command):
    coro = [send_show(dev, command) for dev in devices]
    result = await asyncio.gather(*coro, return_exceptions=True)
    return result


if __name__ == "__main__":
    output = asyncio.run(run_all(devices, "sh clock"))
    pprint(output)
