import asyncio
from datetime import datetime
import random


async def configure_router(ip, commands):
    print(f"Connect to router {ip}")
    await asyncio.sleep(random.random())
    print(f"enable {ip}")
    await asyncio.sleep(random.random())
    print(f"conf t {ip}")
    await asyncio.sleep(random.random())
    for command in commands:
        print(f"Send command {command} {ip}")
        await asyncio.sleep(random.random())
    print(f"end {ip}")
    return ip


async def main():
    ip_list = list(range(1, 11))
    start = datetime.now()
    print(f"Start {datetime.now()}")
    coros = [configure_router(ip, ["command1", "command2"]) for ip in ip_list]
    results = await asyncio.gather(*coros)
    print(f"End {datetime.now() - start}")
    print(f"{results=}")


asyncio.run(main())
