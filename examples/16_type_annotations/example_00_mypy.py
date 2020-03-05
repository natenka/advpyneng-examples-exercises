# https://pyneng2.readthedocs.io/en/latest/book/02_oop_special_methods/add_method.html
from __future__ import annotations
import yaml
import sys
from netmiko import ConnectHandler, NetMikoAuthenticationException
import ipaddress

### example 1


class IPAddress:
    def __init__(self, ip: str) -> None:
        self.ip = ip

    def __str__(self) -> str:
        return f"IPAddress: {self.ip}"

    def __repr__(self) -> str:
        return f"IPAddress('{self.ip}')"


#    def __add__(self, other: int) -> IPAddress:
#        result = self.ip + other
#        return IPAddress(result)

ip1 = IPAddress("10.1.1.1")


### example 2
from typing import Tuple, List, Iterator


class IPv4Network:
    def __init__(self, network: str) -> None:
        self._net = ipaddress.ip_network(network)
        self.address = str(self._net.network_address)
        self.mask = self._net.prefixlen
        self.allocated: Tuple[str, ...] = tuple()

    def hosts(self) -> Tuple[str, ...]:
        return tuple([str(ip) for ip in self._net.hosts()])

    def allocate(self, ip: str) -> None:
        self.allocated += (ip,)

    def unassigned(self) -> Tuple[str, ...]:
        return tuple([ip for ip in self.hosts() if ip not in self.allocated])

    def __iter__(self) -> Iterator:
        return iter(self.hosts())


class IPv4Network2:
    def __init__(self, network: str) -> None:
        self._net = ipaddress.ip_network(network)
        self.address = str(self._net.network_address)
        self.mask = self._net.prefixlen
        self.allocated: List[str] = []

    def hosts(self) -> List[str]:
        return [str(ip) for ip in self._net.hosts()]

    def allocate(self, ip: str) -> None:
        self.allocated.append(ip)

    def unassigned(self) -> List[str]:
        return [ip for ip in self.hosts() if ip not in self.allocated]


### example 3 key type
from typing import Dict, Tuple


class Topology:
    def __init__(self, topology_dict: Dict[Tuple[str, str], Tuple[str, str]]) -> None:
        self.topology = topology_dict.copy()

    def __getitem__(self, item: Tuple[str, str]) -> Tuple[str, str]:
        return self.topology[item]


topology = {("a", "b"): ("c", "d")}
t1 = Topology(topology)


### example 4 optional
from typing import Dict, Union


def send_show_command(device: Dict[str, str], command: str) -> Union[str, None]:
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result
    except NetMikoAuthenticationException as error:
        print(error)
        return None


def main(devices_filename: str, command: str) -> None:
    with open(devices_filename) as f:
        devices: List[Dict[str, str]] = yaml.safe_load(f)
        # devices = yaml.safe_load(f)
    for dev in devices:
        hostname = dev["host"]
        output = send_show_command(dev, command)
        result = hostname + output
        print(result)
