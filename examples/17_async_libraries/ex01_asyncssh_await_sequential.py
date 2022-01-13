from random import choice
from pprint import pprint
import asyncio
import asyncssh
import yaml


async def connect_ssh(device, command):
    print(f"Подключаюсь к {device['host']}")
    ssh = await asyncssh.connect(**device)
    writer, reader, stderr = await ssh.open_session(term_type="xterm")
    await reader.readuntil(">")
    writer.write("enable\n")
    await reader.readuntil("Password")
    writer.write("cisco\n")
    await reader.readuntil("#")
    writer.write("terminal length 0\n")
    await reader.readuntil("#")
    sleep_sec = choice([4, 1, 5])
    print(f"Посплю {sleep_sec} секунд")
    await asyncio.sleep(sleep_sec)
    print(f'Отправляю команду {command} на {device["host"]}')
    writer.write(command + "\n")
    output = await reader.readuntil("#")
    ssh.close()
    print(f'Получили данные от {device["host"]}')
    return output


async def send_command_to_devices(devices, command):
    result1 = await connect_ssh(devices[0], command)
    result2 = await connect_ssh(devices[1], command)
    result3 = await connect_ssh(devices[2], command)
    return [result1, result2, result3]


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    results = asyncio.run(send_command_to_devices(devices, "sh ip int br"))
    pprint(results, width=120)
