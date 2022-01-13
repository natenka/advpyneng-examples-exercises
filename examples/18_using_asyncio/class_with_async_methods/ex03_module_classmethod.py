from pprint import pprint
import asyncio
from itertools import repeat
import re
import asyncssh


class CiscoSSH:
    @classmethod
    async def connect(cls, ip, username, password):
        self = CiscoSSH()

        self.ip = ip
        self.username = username
        self.password = password

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
        return self

    async def send_show_command(self, command):
        print(f"Отправляю команду {command} на устройство {self.ip}")
        self.writer.write(command + "\n")
        output = await self.reader.readuntil([">", "#"])
        return output

    def parse_output(self, command_output):
        m = re.search("(\S+)[#>]", command_output)
        if m:
            return m.group(1)

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
