from pprint import pprint
import asyncio
from itertools import repeat

import asyncssh


async def connect_ssh(ip, command, username="cisco", password="cisco"):
    print(f"Подключаюсь к {ip}")
    async with asyncssh.connect(
        ip,
        username=username,
        password=password,
        encryption_algs="+aes128-cbc,aes256-cbc",
    ) as ssh:
        async with await ssh.create_process() as process:
            print(f"Отправляю команду {command} на устройство {ip}")
            output = await process.stdout.readuntil(">")
            process.stdin.write(command + "\n")
            output = await process.stdout.readuntil(">")
            return output


async def send_command_to_devices(ip_list, command):
    coroutines = map(connect_ssh, ip_list, repeat(command))
    result = await asyncio.gather(*coroutines, return_exceptions=True)
    return result


if __name__ == "__main__":
    # ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    ip_list = ["192.168.100.1"]
    result = asyncio.run(send_command_to_devices(ip_list, "sh ip int br"))
    pprint(result, width=120)
