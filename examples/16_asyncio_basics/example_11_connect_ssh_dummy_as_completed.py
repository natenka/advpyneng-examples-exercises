import asyncio
import time
from datetime import datetime
import random


async def connect_ssh(ip, command):
    print(f"Подключаюсь к {ip}")
    await asyncio.sleep(1)
    print(f"Отправляю команду {command}")
    await asyncio.sleep(random.random() * 10)
    print(f"Получен результат от {ip}")
    return ip, command


async def write_to_file(filename, data):
    print(f">>> Записываю результат в файл {filename}")
    await asyncio.sleep(2)
    print(f"<<< Результат записан в файл {filename}")


async def main():
    ip_list = ["10.1.1.1", "10.1.1.2", "10.1.1.3", "10.1.1.4"]
    coroutines = [connect_ssh(ip, "sh clock") for ip in ip_list]
    tasks = []
    for coro in asyncio.as_completed(coroutines):
        result = await coro
        tasks.append(asyncio.create_task(write_to_file(f"{result[0]}.txt", result)))
    await asyncio.gather(*tasks)


asyncio.run(main())
