from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class NetworkDevice:
    hostname: str
    ios: str
    vendor: str
    ip: str

    def info(self):
        print(f"Device: {self.hostname}")



r1 = NetworkDevice("r1", "15.4", "Cisco", "10.1.1.1")
r2 = NetworkDevice("r2", "12.4", "Cisco", "10.1.1.2")
r3 = NetworkDevice("r3", "15.6", "Cisco", "10.1.1.3")
r4 = NetworkDevice("r4", "15.4", "Cisco", "10.1.1.4")
r5 = NetworkDevice("r1", "15.4", "Cisco", "10.1.1.1")


devices = [r1, r2, r4, r5, r3]

data = [
    ["sw1", "12.5", "Cisco IOS", "10.1.1.101"],
    ["sw2", "12.5", "Cisco IOS", "10.1.1.102"],
    ["sw3", "12.5", "Cisco IOS", "10.1.1.103"],
    ["sw4", "12.5", "Cisco IOS", "10.1.1.104"],
]
