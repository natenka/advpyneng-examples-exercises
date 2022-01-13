from itertools import repeat
from random import choice
from pprint import pprint
import asyncio
import aiofiles
import asyncssh
import yaml


async def connect_ssh(device, command):
    print(f"Подключаюсь к {device['host']}")
    ssh_coroutine = asyncssh.connect(**device)
    ssh = await asyncio.wait_for(ssh_coroutine, timeout=10)
    writer, reader, stderr = await ssh.open_session(
        term_type="Dumb", term_size=(24, 80)
    )
    await reader.readuntil(">")
    writer.write("enable\n")
    await reader.readuntil("Password")
    writer.write("cisco\n")
    await reader.readuntil("#")
    writer.write("terminal length 0\n")
    await reader.readuntil("#")
    sleep_sec = choice([4, 1, 8])
    print(f"Посплю {sleep_sec} секунд")
    await asyncio.sleep(sleep_sec)
    print(f'Отправляю команду {command} на {device["host"]}')
    writer.write(command + "\n")
    output = await reader.readuntil("#")
    ssh.close()
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
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    results = asyncio.run(send_command_to_devices(devices, "sh ip int br"))
    pprint(results, width=120)
