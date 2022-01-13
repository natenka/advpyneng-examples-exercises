import ipaddress


class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def __add__(self, other):
        ip_int = int(ipaddress.ip_address(self.ip))
        sum_ip_str = str(ipaddress.ip_address(ip_int + other))
        return IPAddress(sum_ip_str)


class IPv4Network:
    def __init__(self, network):
        self.network = network

    def hosts(self):
        return list(ipaddress.ip_network(self.network).hosts())
