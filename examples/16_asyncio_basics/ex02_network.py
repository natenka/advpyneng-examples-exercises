import asyncio
from pprint import pprint
import random


async def send_show(device_ip, show_command):
    print(f">>> Start send_show {device_ip}")
    await asyncio.sleep(random.choice([0, 1, 2]))
    print(f"Send command {show_command}")
    await asyncio.sleep(1)
    print(f"<<< End  send_show  {device_ip}")
    return f"{device_ip} {show_command}"


async def get_show_from_devices(devices, command):
    tasks = [asyncio.create_task(send_show(dev, command)) for dev in devices]
    pprint(tasks)
    results = []
    for task in tasks:
        res = await task
        results.append(res)
        pprint(tasks)
    return results


if __name__ == "__main__":
    command_output = asyncio.run(get_show_from_devices([1, 2, 3], "sh clock"))
