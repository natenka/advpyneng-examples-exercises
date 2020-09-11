import ipaddress
from mixin_code import SourceCodeMixin


class Network(SourceCodeMixin):
    def __init__(self, network):
        self.network = network
        self._hosts = [str(ip) for ip in ipaddress.ip_network(network).hosts()]

    def __len__(self):
        return len(self._hosts)

    def __getitem__(self, index):
        return self._hosts[index]
