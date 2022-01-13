from pprint import pprint
import asyncio
from scrapli.driver.core import AsyncIOSXEDriver


async def send_show(device, command):
    async with AsyncIOSXEDriver(**device) as conn:
        result = await conn.send_command(command)
    return result.result


async def send_command_to_devices(devices, command):
    coroutines = [send_show(device, command) for device in devices]
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    common_params = {
        "auth_username": "cisco",
        "auth_password": "cisco",
        "auth_secondary": "cisco",
        "auth_strict_key": False,
        "transport": "asyncssh",
    }
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    devices = [{"host": ip, **common_params} for ip in ip_list]
    result = asyncio.run(send_command_to_devices(devices, "sh ip int br"))
    pprint(result, width=120)

