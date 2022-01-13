import csv
from collections import namedtuple


with open("rib.table.lg.ba.ptt.br-BGP.csv") as f:
    parsed = csv.DictReader(f)
    nhop_45 = (route for route in parsed if route["nexthop"] == "200.219.145.45")
    mask_22 = (route for route in nhop_45 if route["netmask"] == "22")
    for _ in range(4):
        print(next(mask_22))

## Пример с namedtuple

headers = [
    "status",
    "network",
    "netmask",
    "nexthop",
    "metric",
    "locprf",
    "weight",
    "path",
    "origin",
]
with open("rib.table.lg.ba.ptt.br-BGP.csv") as f:
    Route = namedtuple("Route", headers)
    parsed = map(Route._make, csv.reader(f))
    nhop_45 = (route for route in parsed if route.nexthop == "200.219.145.45")
    mask_22 = (route for route in nhop_45 if route.netmask == "22")
    for _ in range(4):
        print(next(mask_22))

