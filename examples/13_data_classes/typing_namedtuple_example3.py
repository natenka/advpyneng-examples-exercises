from typing import NamedTuple
import ipaddress
from pprint import pprint


class IPAddress(NamedTuple):
    ip: str
    mask: int

    def to_int(self):
        return int(ipaddress.ip_address(self.ip))

    def __lt__(self, other):
        return self.to_int() < other.to_int()



ip1 = IPAddress("10.1.1.1", 24)
ip2 = IPAddress("10.10.1.2", 24)
ip3 = IPAddress("10.11.1.3", 24)
ip4 = IPAddress("10.20.1.4", 24)
ip5 = IPAddress("10.2.1.1", 24)

ip_list = [ip1, ip2, ip3, ip4, ip5]
pprint(sorted(ip_list))

# pprint(sorted(ip_list, key=lambda x: ipaddress.ip_address(x.ip)))
