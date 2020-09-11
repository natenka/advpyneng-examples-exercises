import ipaddress
import subprocess
from typing import Union


# def ping_ip(ip_address: ipaddress.IPv4Address) -> bool:
def ping_ip(ip_address: Union[str, ipaddress.IPv4Address]) -> bool:
    reply = subprocess.run(
        ["ping", "-c", "3", "-n", str(ip_address)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    if reply.returncode == 0:
        return True
    else:
        return False


ip1 = ipaddress.ip_address("10.1.1.1")
print(ping_ip(ip1))
print(ping_ip("8.8.8.8"))
print(ping_ip("a"))
