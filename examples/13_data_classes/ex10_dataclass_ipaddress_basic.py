import ipaddress
from dataclasses import dataclass, field

@dataclass(order=True)
class IPAddress:
    ip: str
    mask: int = 24


ip1 = IPAddress("10.1.1.1", 24)
ip2 = IPAddress("10.10.1.2", 24)
ip3 = IPAddress("10.11.1.3", 24)
ip4 = IPAddress("10.20.1.4", 24)
ip5 = IPAddress("10.2.1.1", 24)

ip_list = [ip1, ip2, ip3, ip4, ip5]

