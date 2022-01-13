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
            parsed = reply.textfsm_parse_output()
        return parsed
    except ScrapliException as error:
        print(error)



async def run_all(devices, command):
    coro = [send_show(dev, command) for dev in devices]
    result = await asyncio.gather(*coro, return_exceptions=True)
    return  result


if __name__ == "__main__":
    with open("devices_scrapli_telnet.yaml") as f:
        devices = yaml.safe_load(f)
    output = asyncio.run(run_all(devices, "show ip int br"))
    pprint(output)

