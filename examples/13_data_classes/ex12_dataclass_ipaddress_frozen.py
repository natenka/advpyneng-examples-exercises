import ipaddress
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class IPAddress:
    ip: str = field(compare=False)
    mask: int = 24

    def __post_init__(self):
        print("post init")
        try:
            if self.mask not in range(0, 33):
                raise ValueError("Маска должна быть в range(0, 33)")
        except ValueError:
            raise ValueError("Маска должна быть числом")


ip1 = IPAddress("10.1.1.1", 28)
ip2 = IPAddress("10.10.1.2", 20)
ip3 = IPAddress("10.11.1.3", 24)
ip4 = IPAddress("10.20.1.4", 32)
ip5 = IPAddress("10.2.1.1", 24)

ip_list = [ip1, ip2, ip3, ip4, ip5]

