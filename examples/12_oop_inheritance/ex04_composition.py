class Network:
    def __init__(self, network):
        self.network = network
        self.hosts = ["10.1.1.1", "10.1.1.2"]


class ScanNetwork:
    def __init__(self, network):
        self.network = network

    def ping_all(self):
        for ip in self.network.hosts:
            print(ip)


net1 = Network("10.1.1.0/24")
scanner = ScanNetwork(net1)
scanner.ping_all()

