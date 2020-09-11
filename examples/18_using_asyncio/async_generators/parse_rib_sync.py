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


def open_csv(filename):
    with open(filename) as f:
        for idx, line in enumerate(csv.DictReader(f), 1):
            # print('open_csv', idx)
            yield idx, line


def filter_prefix_next_hop(iterable, nexthop):
    for idx, line in iterable:
        if line["nexthop"] == nexthop:
            yield idx, line


def filter_prefix_mask(iterable, mask):
    for idx, line in iterable:
        if int(line["netmask"]) == mask:
            yield idx, line


if __name__ == "__main__":
    data = open_csv("rib.table.lg.ba.ptt.br-BGP.csv")
    nexthop_45 = filter_prefix_next_hop(data, "200.219.145.45")
    nexthop_45_mask_22 = filter_prefix_mask(nexthop_45, 22)
    for _ in range(3):
        print(next(nexthop_45_mask_22))
