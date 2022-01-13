import asyncio
import time
from datetime import datetime
import random
import logging

logging.basicConfig(
    format='%(asctime)s %(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.DEBUG,
)


async def connect_ssh(ip, command):
    print(f"Подключаюсь к {ip}")
    await asyncio.sleep(1)
    print(f"Отправляю команду {command}")
    time.sleep(1)
    # await asyncio.sleep(1)
    print(f"Получен результат от {ip}")
    return f"{ip}: {command}"


async def main():
    ip_list = ["10.1.1.1", "10.1.1.2", "10.1.1.3", "10.1.1.4"]
    coroutines = [connect_ssh(ip, "sh clock") for ip in ip_list]
    result = await asyncio.gather(*coroutines)
    print(f"{result=}")


asyncio.run(main(), debug=True)
