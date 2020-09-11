import re
from pprint import pprint
import asyncio

import aiofiles


async def get_one_neighbor(filename):
    async with aiofiles.open(filename) as f:
        line = ""
        while True:
            while not "Device ID" in line:
                line = await f.readline()
            neighbor = line
            # async for line in f:
            while True:
                try:
                    line = await f.__anext__()
                    if "----------" in line:
                        break
                    neighbor += line
                except StopAsyncIteration:
                    break
            yield neighbor
            line = await f.readline()
            if not line:
                return


def parse_neighbor(output):
    regex = (
        r"Device ID: (\S+).+?"
        r" IP address: (?P<ip>\S+).+?"
        r"Platform: (?P<platform>\S+ \S+), .+?"
        r", Version (?P<ios>\S+),"
    )

    result = {}
    match = re.search(regex, output, re.DOTALL)
    if match:
        device = match.group(1)
        result[device] = match.groupdict()
    return result


async def main():
    cdp_filename = "sh_cdp_neighbors_detail_sw1.txt"
    async for neighbor in get_one_neighbor(cdp_filename):
        print(parse_neighbor(neighbor))


if __name__ == "__main__":
    asyncio.run(main())
