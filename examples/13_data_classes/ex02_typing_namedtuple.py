from typing import NamedTuple

class NetworkDevice(NamedTuple):
    hostname: str
    ip: str
    ios: str = "15.4"
    vendor: str = "Cisco"

    def __str__(self):
        return f"{self.ip}"


r1 = NetworkDevice("r1", "15.4", "10.1.1.1", "cisco")

