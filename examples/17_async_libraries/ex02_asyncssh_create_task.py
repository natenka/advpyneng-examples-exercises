from random import choice
from pprint import pprint
import asyncio
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
    task_1 = asyncio.create_task(connect_ssh(devices[0], command))
    task_2 = asyncio.create_task(connect_ssh(devices[1], command))
    task_3 = asyncio.create_task(connect_ssh(devices[2], command))
    result1 = await task_1
    result2 = await task_2
    result3 = await task_3
    return [result1, result2, result3]


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    results = asyncio.run(send_command_to_devices(devices, "sh ip int br"))
    pprint(results, width=120)
