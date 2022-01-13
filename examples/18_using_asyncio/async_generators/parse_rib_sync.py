"""
"status","network","netmask","nexthop","metric","locprf","weight","path","origin"
"*","1.0.0.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 15169","i"
"*>","1.0.0.0","24","200.219.145.23",NA,NA,0,"53242 7738 15169","i"
"*","1.0.4.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
"*>","1.0.4.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 7545 56203","i"
"*","1.0.5.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
"""

import csv
from collections import namedtuple
import asyncio
import aiofiles


async def open_csv(filename):
    async with aiofiles.open(filename) as f:
        headers = await f.readline()
        headers = list(csv.reader([headers]))[0]
        print(f"{headers=}")

        index = 1
        async for line in f:
            await asyncio.sleep(0.1)
            dict_line = list(csv.DictReader([line], fieldnames=headers))[0]
            # print('open_csv', idx)
            yield index, dict_line
            index += 1


async def filter_prefix_next_hop(iterable, nexthop):
    async for idx, line in iterable:
        if line["nexthop"] == nexthop:
            yield idx, line


async def filter_prefix_mask(iterable, mask):
    async for idx, line in iterable:
        if int(line["netmask"]) == mask:
            yield idx, line


async def dummy():
    for _ in range(200):
        print("start")
        await asyncio.sleep(0.5)
        print("stop")


async def filter_data():
    data = open_csv("rib.table.lg.ba.ptt.br-BGP.csv")
    nexthop_45 = filter_prefix_next_hop(data, "200.219.145.45")
    nexthop_45_mask_22 = filter_prefix_mask(nexthop_45, 22)
    async for item in nexthop_45_mask_22:
        print(item)

async def main():
    task1 = asyncio.create_task(filter_data())
    task2 = asyncio.create_task(dummy())
    await task1
    await task2


if __name__ == "__main__":
    asyncio.run(main())

