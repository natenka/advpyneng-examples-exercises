import asyncio
import yaml
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
from devices_scrapli import devices as devices_ssh

class CheckConnection:
    def __init__(self, device_list):
        self.device_list = device_list
        self._index = 0

    async def _scan(self, device):
        host = device["host"]
        try:
            async with AsyncScrapli(**device) as conn:
                prompt = await conn.get_prompt()
            return True, prompt
        except ScrapliException as error:
            return False, error

    async def __anext__(self):
        if self._index >= len(self.device_list):
            raise StopAsyncIteration
        device = self.device_list[self._index]
        result = await self._scan(device)
        self._index += 1
        return result

    def __aiter__(self):
        return self

async def scanner(devices, protocol):
    ssh_check = CheckConnection(devices)
    async for status, msg in ssh_check:
        print(f"{protocol} {status} {msg}")


async def main():
    with open("devices_scrapli_telnet.yaml") as f:
        devices_telnet = yaml.safe_load(f)
    scan_ssh = scanner(devices_ssh, "SSH")
    scan_telnet = scanner(devices_telnet, "Telnet")
    await asyncio.gather(scan_ssh, scan_telnet)


if __name__ == "__main__":
    asyncio.run(main())
