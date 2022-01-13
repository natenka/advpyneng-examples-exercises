from pprint import pprint
import asyncio

import yaml
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException


async def send_show(device, show_command):
    try:
        async with AsyncScrapli(**device) as ssh:
            reply = await ssh.send_command(show_command)
            return reply.result
    except ScrapliException as error:
        print(error, device["host"])


async def send_command_to_devices(devices, commands):
    result_dict = {}
    coroutines = [send_show(device, commands) for device in devices]
    all_results = await asyncio.gather(*coroutines)
    for dev, res in zip(devices, all_results):
        result_dict[dev["host"]] = res
    return result_dict


if __name__ == "__main__":
    with open("devices_async.yaml") as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(send_command_to_devices(devices, "sh ip int br"))
    pprint(result, width=120)
