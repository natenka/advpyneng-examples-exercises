import itertools as it
from dataclasses import dataclass
import operator
from pprint import pprint


@dataclass(frozen=True, order=True)
class Network:
    hostname: str
    ios: str
    vendor: str


devices = [
    Network("r1", "12.5", "Cisco IOS"),
    Network("r2", "12.4", "Cisco IOS"),
    Network("r3", "12.4XR", "Cisco XR"),
    Network("r4", "12.5XR", "Cisco XR"),
    Network("r5", "12.5XR", "Cisco XR"),
    Network("r6", "12.5", "Cisco IOS"),
    Network("r7", "12.4", "Cisco IOS"),
]

key = operator.attrgetter("vendor")

sorted_devices = sorted(devices, key=key)
data = it.groupby(sorted_devices, key)

for vendor, devs in data:
    print(vendor)
    pprint(list(devs))

# Cisco IOS            [Network(hostname='r1', ios='12.5', vendor='Cisco IOS'), Network(hostname='r2', ios='12.4', vendor='Cisco IOS'), Network(hostname='r6', ios='12.5', vendor='Cisco IOS'), Network(hostname='r7', ios='12.4', vendor='Cisco IOS')]
# Cisco XR             [Network(hostname='r3', ios='12.4XR', vendor='Cisco XR'), Network(hostname='r4', ios='12.5XR', vendor='Cisco XR'), Network(hostname='r5', ios='12.5XR', vendor='Cisco XR')]
