import asyncio
import logging

from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
from async_timeout import timeout
from rich.logging import RichHandler

from devices_scrapli import devices_telnet, devices_ssh


logging.getLogger("scrapli").setLevel(logging.WARNING)
logging.getLogger("asyncssh").setLevel(logging.WARNING)

logging.basicConfig(
    format="%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="[%X]",
    handlers=[RichHandler()],
)


async def check_connection(devices_list):
    for device in devices_list:
        ip = device["host"]
        transport = device.get("transport")
        try:
            async with timeout(5):  # для asynctelnet
                async with AsyncScrapli(**device) as conn:
                    prompt = await conn.get_prompt()
                yield True, f"{ip=} {prompt=} {transport=}"
        except (ScrapliException, asyncio.exceptions.TimeoutError) as error:
            yield False, f"{ip=} {error=} {transport=}"


async def scan(devices):
    check = check_connection(devices)
    async for status, msg in check:
        if status:
            logging.info(f"Подключение успешно {msg}")
        else:
            logging.warning(f"Не удалось подключиться {msg}")


async def scan_all(telnet_list, ssh_list):
    await asyncio.gather(scan(telnet_list), scan(ssh_list))


if __name__ == "__main__":
    # asyncio.run(scan(devices))
    asyncio.run(scan_all(devices_telnet, devices_ssh))
