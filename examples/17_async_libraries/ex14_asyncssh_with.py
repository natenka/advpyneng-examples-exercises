from pprint import pprint
import asyncio
import asyncssh


async def read_until(reader, line, timeout=3):
    try:
        return await asyncio.wait_for(reader.readuntil(line), timeout)
    except asyncio.TimeoutError as error:
        output = ""
        while True:
            try:
                output += await asyncio.wait_for(reader.read(1000), 0.1)
            except asyncio.TimeoutError as error:
                break
        print(
            f"TimeoutError при выполнении reader.readuntil('{line}')\n"
            f"Последний вывод:"
        )
        print(output)


async def send_show(host, username, password, enable_password, command):
    print(f"Подключение к {host}")
    async with asyncssh.connect(
        host=host,
        username=username,
        password=password,
        encryption_algs="+aes128-cbc,aes256-cbc",
    ) as ssh:
        writer, reader, stderr = await ssh.open_session(
            term_type="Dumb", term_size=(200, 24)
        )
        await read_until(reader, ">")
        writer.write("enable\n")
        await read_until(reader, "Password")
        writer.write(f"{enable_password}\n")
        await read_until(reader, [">", "#"])
        writer.write("terminal length 0\n")
        await read_until(reader, "#")

        print(f"Отправка команды {command} на {host}")
        writer.write(f"{command}\n")
        output = await read_until(reader, "#")
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

