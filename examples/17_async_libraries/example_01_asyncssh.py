from pprint import pprint
import asyncio
import asyncssh
import random

import yaml
from rich import inspect
import aiofiles

async def send_show(device, show):
    secret = device.pop("secret")
    ip = device["host"]
    print(f"Подключаюсь к {ip}")
    async with asyncssh.connect(**device) as ssh:
        writer, reader, _ = await ssh.open_session(term_type="xterm")
        await reader.readuntil(">")
        writer.write("enable\n")
        await reader.readuntil("Password")
        writer.write(f"{secret}\n")
        await reader.readuntil("#")
        writer.write(f"terminal length 0\n")
        await reader.readuntil("#")
        writer.write(f"{show}\n")
        output = await reader.readuntil("#")
        print(f"Получили вывод от {ip}")
        return ip, output

async def write_to_file(ip, out, cmd):
    print(f">>> Запись в файл {ip}")
    filename = ip.replace(".", "_") + cmd.replace(" ", "_") + ".txt"
    async with aiofiles.open(filename, "w") as f:
        await f.write(out)
    print(f">>> Записали      {ip}")


async def run_all(devices, show):
    coroutines = [send_show(dev, show) for dev in devices]
    result = asyncio.as_completed(coroutines)
    for co in result:
        ip, out = await co
        print(f"{ip=} {out=}")
        await write_to_file(ip, out, show)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        r1 = devices[0]
    pprint(asyncio.run(run_all(devices, "sh clock")), sort_dicts=False)
