import ipaddress
from pprint import pprint
from dataclasses import dataclass, field


@dataclass(order=True)
class IPAddress:
    ip: str = field(compare=False)
    _ip: int = field(init=False, repr=False)
    mask: int

    def __post_init__(self):
        print("__post_init__")
        self._ip = int(ipaddress.ip_address(self.ip))

    def __add__(self, other):
        print("Вызывается __add__")
        if not isinstance(other, int):
            raise TypeError(
                f"unsupported operand type(s) for +: "
                f"'IPAddress' and '{type(other).__name__}'"
            )
        new_ip = self._ip + other
        new_ip_str = str(ipaddress.ip_address(new_ip))
        return IPAddress(new_ip_str)


ip1 = IPAddress("10.1.1.1", "24")
ip2 = IPAddress("10.10.1.2", 24)
ip3 = IPAddress("10.11.1.3", 24)
ip4 = IPAddress("10.20.1.4", 24)
ip5 = IPAddress("10.2.1.1", 24)

ip_list = [ip1, ip2, ip3, ip4, ip5]
pprint(sorted(ip_list))
