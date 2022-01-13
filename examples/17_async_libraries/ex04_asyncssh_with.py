from pprint import pprint
import asyncio
from itertools import repeat

import asyncssh


async def connect_ssh(ip, command, username="cisco", password="cisco"):
    print(f"Подключаюсь к {ip}")
    #if ip == "192.168.100.1": password = "cisco123"
    async with asyncssh.connect(
        ip,
        username=username,
        password=password,
        encryption_algs="+aes128-cbc,aes256-cbc",
        # login_timeout=5
    ) as ssh:
        writer, reader, stderr = await ssh.open_session(
            term_type="Dumb", term_size=(200, 24)
        )
        output = await reader.readuntil(">")
        writer.write("enable\n")
        output = await reader.readuntil("Password")
        writer.write("cisco\n")
        output = await reader.readuntil("#")
        writer.write("terminal length 0\n")
        output = await reader.readuntil("#")

        print(f"Отправляю команду {command} на устройство {ip}")
        writer.write(command + "\n")
        output = await reader.readuntil([">", "#"])
    return output


async def send_command_to_devices(ip_list, command):
    coroutines = map(connect_ssh, ip_list, repeat(command))
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    result = asyncio.run(send_command_to_devices(ip_list, "sh clock"))
    pprint(result)
