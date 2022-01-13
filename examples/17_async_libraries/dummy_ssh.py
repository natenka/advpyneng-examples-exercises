import asyncio
from datetime import datetime
import random


async def configure_router(ip):
    print(f"Connect to router {ip}")
    await asyncio.sleep(random.random() * 2)
    print(f"end {ip}")
    return ip


async def main():
    ip_list = range(100)
    start = datetime.now()
    print(f"Start {datetime.now()}")
    coros = [configure_router(ip) for ip in ip_list]
    results = await asyncio.gather(*coros)
    print(f"End {datetime.now() - start}")
    print(f"{results=}")


if __name__ == "__main__":
    asyncio.run(main())
