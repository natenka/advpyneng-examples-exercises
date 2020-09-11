import ipaddress


class IPv4Network:
    def __init__(self, network):
        self._net = ipaddress.ip_network(network)
        self.address = str(self._net.network_address)
        self.mask = self._net.prefixlen
        self.allocated = tuple()

    def hosts(self):
        return tuple([str(ip) for ip in self._net.hosts()])

    def allocate(self, ip):
        # if not ip in self.hosts():
        #    raise ValueError(f'Адрес должен быть из сети '
        #                     f'{self.address}/{self.mask}')
        self.allocated += (ip,)

    def unassigned(self):
        return tuple([ip for ip in self.hosts() if ip not in self.allocated])
