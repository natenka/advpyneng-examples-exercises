from collections import namedtuple


NetworkDevice = namedtuple("NetworkDevice", "hostname ios ip vendor")

r1 = NetworkDevice("r1", "15.2", "10.1.1.1", "Cisco")
r2 = NetworkDevice("r2", "15.2", "10.1.1.2", "Cisco")
r3 = NetworkDevice("r3", "15.4", "10.1.1.3", "Cisco")
r4 = NetworkDevice("r4", "15.2", "10.1.1.4", "Cisco")
