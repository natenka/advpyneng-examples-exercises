"""
Код нужен только как стартовая заготовка, он будет исправлен на лекции
"""
from pprint import pprint
import asyncio
from itertools import repeat

import asyncssh


class CiscoSSH:
    def __init__(self, ip, username, password, enable_password):
        self.ip = ip
        self.username = username
        self.password = password
        self.enable_password = enable_password

    async def connect(self):
        print(f"Подключаюсь к {self.ip}")
        self._ssh = await asyncssh.connect(
            self.ip,
            username=self.username,
            password=self.password,
            encryption_algs="+aes128-cbc,aes256-cbc",
            connect_timeout=5,
        )
        self._writer, self._reader, _ = await self._ssh.open_session(
            term_type="Dumb"
        )
        output = await self.read_until(">")
        self._writer.write("enable\n")
        output = await self.read_until("Password")
        self._writer.write(f"{self.enable_password}\n")
        output = await self.read_until("#")
        self._writer.write("terminal length 0\n")
        output = await self.read_until("#")

    async def read_until(self, prompt, timeout=5):
        try:
            output = await asyncio.wait_for(
                self._reader.readuntil(prompt), timeout
            )
            return output
        except asyncio.TimeoutError:
            print(f"нет {prompt} читаем что-то")
            output = await self._reader.read(10)
            return output

    async def send_show_command(self, command):
        print(f"Отправляю команду {command} на устройство {self.ip}")
        self._writer.write(command + "\n")
        output = await self.read_until("#")
        return output

    def close(self):
        self._ssh.close()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.close()


async def main():
    async with CiscoSSH("192.168.100.1", "cisco", "cisco", "cisco") as r1:
        out = await r1.send_show_command("sh clock")
        print(out)


if __name__ == "__main__":
    asyncio.run(main())
