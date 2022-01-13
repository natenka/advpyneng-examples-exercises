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
    print("run all...")
    coro = [send_show(dev, command) for dev in devices]
    result = await asyncio.gather(*coro, return_exceptions=True)
    print("done...")
    return result


if __name__ == "__main__":
    #output = asyncio.run(run_all(devices, "sh clock"))
    #pprint(output)
    coro = run_all(devices, "sh clock")
    loop = asyncio.new_event_loop()
    task1 = loop.create_task(coro)
    task2 = loop.create_task(asyncio.sleep(5))
    print("sleep...")
    time.sleep(2)
    print(f"{loop.is_running()=}")
    try:
        output = loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
