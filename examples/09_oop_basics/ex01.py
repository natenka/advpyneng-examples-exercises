class IPAddress:
    ip_version = 4
    all_ip_set = set()

    def __init__(self, ip):
        self.ip = ip
        self.self = self
        # self.all_ip_set.add(ip)
        # IPAddress.all_ip_set.add(ip)
        type(self).all_ip_set.add(ip)

    def pprint(self):
        print("IPAddress", self.ip)


