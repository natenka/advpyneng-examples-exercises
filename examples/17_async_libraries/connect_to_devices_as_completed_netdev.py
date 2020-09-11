from itertools import repeat
from random import choice
from pprint import pprint
import asyncio
import aiofiles
import netdev
import yaml


async def connect_ssh(device, command):
    print(f"Подключаюсь к {device['host']}")
    async with netdev.create(**device) as ssh:
        sleep_sec = choice([4, 1, 8])
        print(f"Посплю {sleep_sec} секунд")
        await asyncio.sleep(sleep_sec)
        print(f'Отправляю команду {command} на {device["host"]}')
        output = await ssh.send_command(command)
        print(f'Получили данные от {device["host"]}')
    return (device["host"], command, output)


async def write_to_file(data):
    ip, command, output = data
    print(f"########### Запись в файл для {ip}")
    filename = f"{ip.replace('.', '_')}_{command.replace(' ', '_')}.txt"
    async with aiofiles.open(filename, "w") as f:
        await f.write(output)
    print(f"########### Вывод записан в файл для {ip}")


async def send_command_to_devices(devices, command):
    coroutines = map(connect_ssh, devices, repeat(command))
    print(">>> Запускаем")
    tasks = []
    for future in asyncio.as_completed(coroutines):
        result = await future
        tasks.append(asyncio.create_task(write_to_file(result)))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    results = asyncio.run(send_command_to_devices(devices, "sh run"))
    pprint(results, width=120)
