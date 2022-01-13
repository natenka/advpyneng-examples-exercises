from pprint import pprint

import pytest
from netmiko import Netmiko
import yaml


@pytest.fixture(scope="session")
def cisco_ios_router_common_params():
    data = {
        "device_type": "cisco_ios",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    return data


@pytest.fixture(scope="session")
def cisco_ios_router_reachable():
    data = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    return data


@pytest.fixture(scope="session")
def ssh_connection_cisco_ios(cisco_ios_router_reachable):
    print("\n### SETUP\n")
    with Netmiko(**cisco_ios_router_reachable) as ssh:
        ssh.enable()
        yield ssh
    print("\n### TEARDOWN\n")


@pytest.fixture()
def topology_with_dupl_links():
    topology = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }
    return topology

@pytest.fixture()
def normalized_topology_example():
    normalized_topology = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    }
    return normalized_topology
