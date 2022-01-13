import asyncio
import time
import logging
from concurrent.futures import ThreadPoolExecutor


logging.getLogger("asyncio").setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.DEBUG
)


def netmiko_connect(device):
    logging.info(f"sync Подключаюсь к {device}")
    time.sleep(5)
    logging.info(f"sync Получили результат {device}")
    return device


async def scrapli_connect(device):
    logging.info(f"async Подключаюсь к {device}")
    await asyncio.sleep(1)
    if device == 20:
        for _ in range(10):
            logging.info("waiting...")
            await asyncio.sleep(1)
    logging.info(f"async Получили результат {device}")
    return device


async def main():
    loop = asyncio.get_running_loop()

    devices = list(range(100))
    coroutines = []
    with ThreadPoolExecutor(max_workers=10) as ex:
        for dev in devices:
            if dev % 2:
                # coro = asyncio.to_thread(netmiko_connect, dev)
                coro = loop.run_in_executor(ex, netmiko_connect, dev)
            else:
                coro = scrapli_connect(dev)
            coroutines.append(coro)
        # logging.info(coroutines)
        results = await asyncio.gather(*coroutines)
    return results


if __name__ == "__main__":
    logging.info(asyncio.run(main()))
