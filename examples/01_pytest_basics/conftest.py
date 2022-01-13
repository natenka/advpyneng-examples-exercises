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


with open("devices.yaml") as f:
    DEVICES = yaml.safe_load(f)
DEVICES_IP = [dev["host"] for dev in DEVICES]


def get_host(device):
    return device["host"]


@pytest.fixture(params=DEVICES, ids=get_host, scope="session")
def ssh_connection(request):
    ssh = Netmiko(**request.param)
    ssh.enable()
    yield ssh
    ssh.disconnect()


@pytest.fixture(
    params=["192.168.100.1", "192.168.100.2", "192.168.100.3"],
    scope="module",
)
def ssh_conn(request):
    #print("\n\n>>> SETUP", request.param)
    device = {
        "host": request.param,
        "device_type": "cisco_ios",
        "password": "cisco",
        "secret": "cisco",
        "username": "cisco",
    }
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        yield ssh
    #print("\n\n<<< TEARDOWN", request.param)
