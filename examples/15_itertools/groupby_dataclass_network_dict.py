import itertools as it
import operator
from pprint import pprint


devices = [
    {"hostname": "r1", "ios": "12.5", "vendor": "Cisco IOS"},
    {"hostname": "r2", "ios": "12.4", "vendor": "Cisco IOS"},
    {"hostname": "r3", "ios": "12.4XR", "vendor": "Cisco XR"},
    {"hostname": "r4", "ios": "12.5XR", "vendor": "Cisco XR"},
    {"hostname": "r5", "ios": "12.5XR", "vendor": "Cisco XR"},
    {"hostname": "r6", "ios": "12.5", "vendor": "Cisco IOS"},
    {"hostname": "r7", "ios": "12.4", "vendor": "Cisco IOS"},
]

key = operator.itemgetter("vendor")
# key = lambda x: x.get("vendor")

sorted_devices = sorted(devices, key=key)
pprint(sorted_devices)
data = it.groupby(sorted_devices, key)

for vendor, devs in data:
    print(vendor)
    pprint(list(devs))

