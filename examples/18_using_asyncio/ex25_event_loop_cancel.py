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
            await asyncio.sleep(10)
        return reply.result
    except ScrapliException as error:
        print(error, host)
    except asyncio.CancelledError:
        print(f"Отмена... {host}")
        await asyncio.sleep(2)
        print("Отменено")


async def run_all(devices, command):
    coro = [send_show(dev, command) for dev in devices]
    result = await asyncio.gather(*coro, return_exceptions=True)
    return result


async def cancel_tasks():
    tasks = [task for task in asyncio.all_tasks()
             if task is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    pprint(tasks)
    output = await asyncio.gather(*tasks, return_exceptions=True)
    pprint(output)


if __name__ == "__main__":
    #output = asyncio.run(run_all(devices, "sh clock"))
    #pprint(output)
    loop = asyncio.new_event_loop()
    try:
        output = loop.run_until_complete(run_all(devices, "sh clock"))
        pprint(output)
    except KeyboardInterrupt:
        loop.run_until_complete(cancel_tasks())
    finally:
        loop.close()
