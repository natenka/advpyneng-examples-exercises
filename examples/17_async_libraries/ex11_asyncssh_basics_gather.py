from pprint import pprint
import asyncio
import asyncssh


async def send_show(host, username, password, enable_password, command):
    print(f"Подключение к {host}")
    ssh = await asyncssh.connect(
        host=host,
        username=username,
        password=password,
        encryption_algs="+aes128-cbc,aes256-cbc",
    )
    writer, reader, stderr = await ssh.open_session(
        term_type="Dumb", term_size=(200, 24)
    )
    await reader.readuntil(">")
    writer.write("enable\n")
    await reader.readuntil("Password")
    writer.write(f"{enable_password}\n")
    await reader.readuntil([">", "#"])
    writer.write("terminal length 0\n")
    await reader.readuntil("#")

    print(f"Отправка команды {command} на {host}")
    writer.write(f"{command}\n")
    output = await reader.readuntil("#")
    ssh.close()
    return output


async def send_command_to_devices(devices, command):
    coroutines = [send_show(**device, command=command) for device in devices]
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    devices = [
        {'host': '192.168.100.1',
         'username': 'cisco',
         'password': 'cisco',
         'enable_password': 'cisco'},
        {'host': '192.168.100.2',
         'username': 'cisco',
         'password': 'cisco',
         'enable_password': 'cisco'},
        {'host': '192.168.100.3',
         'username': 'cisco',
         'password': 'cisco',
         'enable_password': 'cisco'},
    ]
    result = asyncio.run(send_command_to_devices(devices, "sh ip int br"))
    pprint(result, width=120)

