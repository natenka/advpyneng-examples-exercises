import ipaddress


class IPAddress:
    def __init__(self, ip):
        self._ip = int(ipaddress.ip_address(ip))

    def __str__(self):
        return f"IPAddress: {self._ip}"

    def __repr__(self):
        return f"IPAddress('{self._ip}')"

    def __eq__(self, other):
        return self._ip == other._ip

    def __lt__(self, other):
        return self._ip < other._ip


if __name__ == "__main__":
    ip1 = IPAddress("10.10.1.1")
    ip2 = IPAddress("10.2.1.1")
    print(ip1 < ip2)
    print(ip1 > ip2)
    print(ip1 >= ip2)
    print(ip1 <= ip2)
    print(ip1 == ip2)
    print(ip1 != ip2)
