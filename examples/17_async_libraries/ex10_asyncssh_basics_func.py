from pprint import pprint
import asyncio
import asyncssh


async def send_show(host, username, password, enable_password, command):
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

    writer.write(f"{command}\n")
    output = await reader.readuntil("#")
    ssh.close()
    return output


if __name__ == "__main__":
    r1 = {
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "enable_password": "cisco",
    }
    result = asyncio.run(send_show(**r1, command="sh ip int br"))
    print(result)

