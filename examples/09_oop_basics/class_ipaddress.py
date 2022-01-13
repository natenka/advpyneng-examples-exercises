import ipaddress
from functools import total_ordering


@total_ordering
class IPAddress:
    ip_type = "IPv4"
    all_addresses = set()

    def __init__(self, ip):
        print("Вызывается __init__")
        self.ip = ip
        self._ip_as_int = int(ipaddress.ip_address(self.ip))
        IPAddress.all_addresses.add(ip)

    def __repr__(self):
        return f"IPAddress('{self.ip}')"

    def __str__(self):
        return self.ip

    def __len__(self):
        print("Вызывается __len__")
        return 42

    def __int__(self):
        print("Вызывается __int__")
        return self._ip_as_int

    def __eq__(self, other): # self == other
        print("Вызывается __eq__")
        if not isinstance(other, IPAddress):
            raise TypeError(
                f"'==' not supported between instances of "
                f"'IPAddress' and '{type(other).__name__}'"
            )
        return int(self) == int(other)

    def __lt__(self, other): # self < other
        print("Вызывается __lt__")
        if not isinstance(other, IPAddress):
            raise TypeError(
                f"'<' not supported between instances of "
                f"'IPAddress' and '{type(other).__name__}'"
            )
        return int(self) < int(other)

    def __add__(self, other):
        print("Вызывается __add__")
        if not isinstance(other, int):
            raise TypeError(
                f"unsupported operand type(s) for +: "
                f"'IPAddress' and '{type(other).__name__}'"
            )
        new_ip = int(self) + other
        new_ip_str = str(ipaddress.ip_address(new_ip))
        return IPAddress(new_ip_str)

    def __radd__(self, other):
        print("Вызывается __radd__", self, other)
        return self + other


ip1 = IPAddress("10.1.1.1")
ip2 = IPAddress("10.2.2.2")
ip3 = IPAddress("10.10.2.2")
ip4 = IPAddress("10.11.2.2")
