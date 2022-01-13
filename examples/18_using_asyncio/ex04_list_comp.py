import asyncio
from pprint import pprint
import yaml
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
from devices_scrapli import devices as devices_ssh


async def send_show(device, command):
    print(f">>> connect to {device['host']}")
    try:
        async with AsyncScrapli(**device) as conn:
            result = await conn.send_command(command)
            print(f"<<< {device['host']}")
            return result.result
    except ScrapliException as error:
        print(error, device["host"])


async def tasks(devices, command):
    for device in devices:
        yield asyncio.create_task(send_show(device, command))


async def send_command_to_devices(devices, command):
    all_tasks = [task async for task in tasks(devices, command)]
    result = [await t for t in all_tasks]
    return result


if __name__ == "__main__":
    with open("devices_scrapli.yaml") as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(send_command_to_devices(devices, "sh clock"))
    pprint(result, width=120)
