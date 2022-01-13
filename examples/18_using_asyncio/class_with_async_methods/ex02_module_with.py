from pprint import pprint
import asyncio
from itertools import repeat

import asyncssh


class CiscoSSH:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password

    async def connect(self):
        print(f"Подключаюсь к {self.ip}")
        ssh_coroutine = asyncssh.connect(
            self.ip,
            username=self.username,
            password=self.password,
            encryption_algs="+aes128-cbc,aes256-cbc",
        )
        self.ssh = await asyncio.wait_for(ssh_coroutine, timeout=10)
        self.writer, self.reader, stderr = await self.ssh.open_session(
            term_type="Dumb", term_size=(200, 24)
        )
        output = await self.reader.readuntil(">")
        self.writer.write("enable\n")
        output = await self.reader.readuntil("Password")
        self.writer.write("cisco\n")
        output = await self.reader.readuntil("#")
        self.writer.write("terminal length 0\n")
        output = await self.reader.readuntil("#")

    async def send_show_command(self, command):
        print(f"Отправляю команду {command} на устройство {self.ip}")
        self.writer.write(command + "\n")
        output = await self.reader.readuntil([">", "#"])
        return output

    async def close(self):
        self.ssh.close()
        await self.ssh.wait_closed()

    async def __aenter__(self):
        print("__aenter__")
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("__aexit__")
        await self.close()
