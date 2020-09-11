import yaml
import pytest
from netmiko import ConnectHandler


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


@pytest.fixture(scope="session")
def device_example():
    r1 = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
        "fast_cli": True,
    }
    return r1


@pytest.fixture(scope="session")
def device_connection(device_example):
    print("\nОткрываю сессию")
    r1 = ConnectHandler(**device_example)
    r1.enable()
    yield r1
    print("\nЗакрываю сессию")
    r1.disconnect()
