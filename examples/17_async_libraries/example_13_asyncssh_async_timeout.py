from pprint import pprint
import asyncio
from itertools import repeat

import asyncssh
from async_timeout import timeout


async def connect_ssh(ip, command, username="cisco", password="cisco"):
    print(f"Подключаюсь к {ip}")
    ssh_coroutine = asyncssh.connect(ip, username=username, password=password)
    # так как нет встроенного таймаута, запускаем через wait_for
    ssh = await asyncio.wait_for(ssh_coroutine, timeout=10)
    writer, reader, stderr = await ssh.open_session(
        term_type="Dumb", term_size=(200, 24)
    )
    async with timeout(20):
        output = await reader.readuntil(">")
        writer.write("enable\n")
        output = await reader.readuntil("Password")
        writer.write("cisco\n")
        output = await reader.readuntil("#")
        # writer.write('terminal length 0\n')
        # output = await reader.readuntil('#')

        print(f"Отправляю команду {command} на устройство {ip}")
        writer.write(command + "\n")
        output = await reader.readuntil([">", "#"])
        ssh.close()
        return output


async def send_command_to_devices(ip_list, command):
    coroutines = map(connect_ssh, ip_list, repeat(command))
    result = await asyncio.gather(*coroutines, return_exceptions=True)
    return result


if __name__ == "__main__":
    # ip_list = ['192.168.100.1', '192.168.100.2', '192.168.100.3']
    ip_list = ["192.168.100.1"]
    result = asyncio.run(send_command_to_devices(ip_list, "sh run"))
    pprint(result, width=120)
