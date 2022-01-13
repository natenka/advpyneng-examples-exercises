

class ScanNetwork:
    def __init__(self, ip_list):
        self.ip_list = ip_list

    def add_ip(self, ip):
        self.ip_list.append(ip)

    def ping_all(self):
        for ip in self.ip_list:
            print(ip)


ip = ["10.1.1.1", "10.2.2.2"]
scanner = ScanNetwork(ip)
scanner.ping_all()
