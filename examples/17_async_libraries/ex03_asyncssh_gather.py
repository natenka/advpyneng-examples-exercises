from pprint import pprint
import asyncio
from itertools import repeat

import asyncssh


async def connect_ssh(ip, command, username="cisco", password="cisco"):
    print(f"Подключаюсь к {ip}")
    # asyncssh.misc.KeyExchangeFailed: No matching encryption algorithm found,
    # sent aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
    # and received aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc
    ssh_coroutine = asyncssh.connect(
        ip,
        username=username,
        password=password,
        encryption_algs="+aes128-cbc,aes256-cbc",
    )
    # так как нет встроенного таймаута, запускаем через wait_for
    ssh = await asyncio.wait_for(ssh_coroutine, timeout=10)
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
    ssh.close()
    return output


async def send_command_to_devices(ip_list, command):
    coroutines = map(connect_ssh, ip_list, repeat(command))
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    # ip_list = ["192.168.100.1"]
    result = asyncio.run(send_command_to_devices(ip_list, "sh ip int br"))
    pprint(result, width=120)
