import asyncio
from itertools import repeat


async def connect_ssh(ip, command):
    print(f"Подключаюсь к {ip}")
    await asyncio.sleep(ip)
    print(f"Отправляю команду {command} на устройство {ip}")
    await asyncio.sleep(1)
    return f"{command} {ip}"


async def send_command_to_devices(ip_list, command):
    coroutines = map(connect_ssh, ip_list, repeat(command))
    result = await asyncio.gather(*coroutines)

    tasks = [asyncio.create_task(connect_ssh(ip, command)) for ip in ip_list]
    results = [await task for task in tasks]
    return result


if __name__ == "__main__":
    ip_list = [5, 2, 3, 7]
    result = asyncio.run(send_command_to_devices(ip_list, "test"))
    print("Result:", result)


# $ python example_04_gather.py
# Подключаюсь к 5
# Подключаюсь к 2
# Подключаюсь к 3
# Подключаюсь к 7
# Отправляю команду test на устройство 2
# Отправляю команду test на устройство 3
# Отправляю команду test на устройство 5
# Отправляю команду test на устройство 7
# Result: ['test 5', 'test 2', 'test 3', 'test 7']
