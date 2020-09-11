import asyncssh
import asyncio
import async_timeout


class BaseSSH:
    def __init__(self, host, username, password, timeout=30):
        self.host = host
        self.username = username
        self.password = password
        self.timeout = timeout
        self._MAX_READ = 10000

    async def connect(self):
        with async_timeout.timeout(self.timeout):
            self._ssh = await asyncssh.connect(
                self.host, username=self.username, password=self.password
            )
            self._writer, self._reader, self._stderr = await self._ssh.open_session(
                term_type="Dumb", term_size=(200, 24)
            )
            await self._reader.readuntil(">")
        return self

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        self._ssh.close()
        await self._ssh.wait_closed()

    async def send_command(self, command):
        self._writer.write(command + "\n")
        output = await self._reader.readuntil([">", "#"])
        return output


async def main():
    async with BaseSSH("192.168.100.1", "cisco", "cisco") as r1:
        output = await r1.send_command("sh ip int br")
        print(output)


if __name__ == "__main__":
    asyncio.run(main())
