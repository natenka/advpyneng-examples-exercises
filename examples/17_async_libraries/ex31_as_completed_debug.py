import asyncio
import random

import logging

logging.basicConfig(level=logging.DEBUG)


async def connect_ssh(ip, command):
    print(f"Подключаюсь к {ip}")
    await asyncio.sleep(random.choice(range(1, 11, 3)))
    if ip == "10.3.3.3":
        raise ValueError("Опасность! Опасность!")
    print(f"Отправляю команду {command} на {ip}")
    await asyncio.sleep(random.random())
    return ip, command


async def write_to_file(data):
    await asyncio.sleep(random.choice(range(1, 11, 3)))
    filename = data[0].replace(".", "_") + ".txt"
    print(f"Записываю в файл {filename} данные {data[1]}")
    await asyncio.sleep(random.choice(range(1, 11, 2)))


async def main():
    command = "sh clock"
    ip_list = ["10.1.1.1", "10.2.2.2", "10.3.3.3", "10.4.4.4", "10.5.5.5", "10.6.6.6"]
    coroutines = [connect_ssh(ip, command) for ip in ip_list]
    tasks = []
    for f in asyncio.as_completed(coroutines):
        try:
            output = await f
            tasks.append(asyncio.create_task(write_to_file(output)))
        except Exception as exc:
            print("Исключение", exc)
    print(">>> Ждем выполнения всех задач")
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main(), debug=True)

"""
$ python example_05_as_completed.py
Подключаюсь к 10.3.3.3
Подключаюсь к 10.5.5.5
Подключаюсь к 10.1.1.1
Подключаюсь к 10.2.2.2
Подключаюсь к 10.6.6.6
Подключаюсь к 10.4.4.4
Отправляю команду sh clock на 10.1.1.1
Исключение Опасность! Опасность!
Отправляю команду sh clock на 10.2.2.2
Отправляю команду sh clock на 10.6.6.6
Записываю в файл 10_2_2_2.txt данные sh clock
Записываю в файл 10_1_1_1.txt данные sh clock
Отправляю команду sh clock на 10.5.5.5
Записываю в файл 10_5_5_5.txt данные sh clock
Отправляю команду sh clock на 10.4.4.4
>>> Ждем выполнения всех задач
Записываю в файл 10_4_4_4.txt данные sh clock
Записываю в файл 10_6_6_6.txt данные sh clock
"""
