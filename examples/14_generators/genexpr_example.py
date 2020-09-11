import csv
from collections import namedtuple


with open("rib.table.lg.ba.ptt.br-BGP.csv") as f:
    parsed = csv.DictReader(f)
    nhop_45 = (route for route in parsed if route["nexthop"] == "200.219.145.45")
    mask_22 = (route for route in nhop_45 if route["netmask"] == "22")
    for _ in range(4):
        print(next(mask_22))
"""
OrderedDict([('status', '*'), ('network', '1.0.28.0'), ('netmask', '22'), ('nexthop', '200.219.145.45'), ('metric', 'NA'), ('locprf', 'NA'), ('weight', '0')                                                                                , ('path', '28135 18881 3549 6762 10026 2519'), ('origin', 'i')])
OrderedDict([('status', '*'), ('network', '1.0.208.0'), ('netmask', '22'), ('nexthop', '200.219.145.45'), ('metric', 'NA'), ('locprf', 'NA'), ('weight', '0'                                                                                ), ('path', '28135 18881 3549 3356 4651 9737 23969'), ('origin', 'i')])
OrderedDict([('status', '*'), ('network', '1.10.128.0'), ('netmask', '22'), ('nexthop', '200.219.145.45'), ('metric', 'NA'), ('locprf', 'NA'), ('weight', '0                                                                                '), ('path', '28135 18881 3549 2914 38040 9737 23969'), ('origin', 'i')])
OrderedDict([('status', '*'), ('network', '1.10.132.0'), ('netmask', '22'), ('nexthop', '200.219.145.45'), ('metric', 'NA'), ('locprf', 'NA'), ('weight', '0                                                                                '), ('path', '28135 18881 3549 2914 38040 9737 23969'), ('origin', 'i')])
"""


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

"""
Route(status='*', network='1.0.28.0', netmask='22', nexthop='200.219.145.45', metric='NA', locprf='NA', weight='0', path='28135 18881 3549 6762 10026 2519',                                                                                 origin='i')
Route(status='*', network='1.0.208.0', netmask='22', nexthop='200.219.145.45', metric='NA', locprf='NA', weight='0', path='28135 18881 3549 3356 4651 9737 2                                                                                3969', origin='i')
Route(status='*', network='1.10.128.0', netmask='22', nexthop='200.219.145.45', metric='NA', locprf='NA', weight='0', path='28135 18881 3549 2914 38040 9737                                                                                 23969', origin='i')
Route(status='*', network='1.10.132.0', netmask='22', nexthop='200.219.145.45', metric='NA', locprf='NA', weight='0', path='28135 18881 3549 2914 38040 9737                                                                                 23969', origin='i')
"""
