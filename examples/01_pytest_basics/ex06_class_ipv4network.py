import ipaddress


class IPv4Network:
    def __init__(self, network):
        self.network = network
        self.mask = int(network.split("/")[-1])
        self.bin_mask = "1" * self.mask + "0" * (32 - self.mask)

    def hosts(self):
        net = ipaddress.ip_network(self.network)
        return [str(ip) for ip in net.hosts()]

    def __repr__(self):
        return f"Network('{self.network}')"

    def __len__(self):
        return len(self.hosts())

    def __iter__(self):
        return iter(self.hosts())


if __name__ == "__main__":
    net1 = IPv4Network("10.1.1.0/26")
    all_hosts = net1.hosts()
    print(all_hosts)
