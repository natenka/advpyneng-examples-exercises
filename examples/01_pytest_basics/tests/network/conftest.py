from pprint import pprint

import pytest
from netmiko import Netmiko
import yaml


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
