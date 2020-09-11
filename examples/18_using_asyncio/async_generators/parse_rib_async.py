"""
"status","network","netmask","nexthop","metric","locprf","weight","path","origin"
"*","1.0.0.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 15169","i"
"*>","1.0.0.0","24","200.219.145.23",NA,NA,0,"53242 7738 15169","i"
"*","1.0.4.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
"*>","1.0.4.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 7545 56203","i"
"*","1.0.5.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
"""

import csv
import asyncio
import aiofiles


async def sleep(sec):
    for _ in range(10):
        print("sleep")
        await asyncio.sleep(sec)
        print("wake up")


async def open_csv(filename):
    async with aiofiles.open(filename) as f:
        headers = await f.readline()
        headers = list(csv.reader([headers]))[0]
        async for line in f:
            print("open_csv line")
            await asyncio.sleep(1)
            yield dict(list(csv.DictReader([line], fieldnames=headers))[0])


async def filter_prefix_next_hop(async_iterable, nexthop):
    async for line in async_iterable:
        if line["nexthop"] == nexthop:
            yield line


async def parse_data(filename):
    data = open_csv(filename)
    nhop_45 = filter_prefix_next_hop(data, "200.219.145.45")
    async for line in nhop_45:
        print("parse_data line")
        print(line)


async def main():
    t1 = asyncio.create_task(sleep(2))
    t2 = parse_data("rib.table.lg.ba.ptt.br-BGP.csv")
    await asyncio.gather(t1, t2)


if __name__ == "__main__":
    asyncio.run(main())
    # nexthop_45 = filter_prefix_next_hop(data, "200.219.145.45")
    # nexthop_45_mask_22 = filter_prefix_mask(nexthop_45, 22)
    # for _ in range(3):
    #    print(next(nexthop_45_mask_22))

    # при использовании asyncio.run появляется исключение, если генератор прерывается,
    # когда он не дошел до конца
    # пофиксили в последних версиях 3.7/3.8
    # https://bugs.python.org/issue38013
