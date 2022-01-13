import asyncio
import time
import logging
import random


logging.getLogger("asyncio").setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.DEBUG
)

async def scrapli_connect(device):
    await asyncio.sleep(random.random() * 10)
    await asyncio.sleep(random.random() * 10)
    return device


async def semaphore_connect(semaphore, func, *args, **kwargs):
    async with semaphore:
        return await func(*args, **kwargs)


async def main():
    sem = asyncio.Semaphore(10000)
    devices = range(10000)
    coroutines = [semaphore_connect(sem, scrapli_connect, dev) for dev in devices]
    results = await asyncio.gather(*coroutines)
    return results


if __name__ == "__main__":
    logging.info(asyncio.run(main()))
