import pytest
import subprocess
from netmiko import ConnectHandler
import yaml

# ================= это должно быть в conftest.py ===============


with open("devices.yaml") as f:
    all_devices = yaml.safe_load(f)

all_hosts = [device["host"] for device in all_devices]


@pytest.fixture(params=all_devices, scope="session")
def one_device_params(request):
    return request.param


@pytest.fixture(params=all_devices, scope="session")
def connect_all(request):
    ssh = ConnectHandler(**request.param)
    ssh.enable()
    yield ssh
    ssh.disconnect()


# ================================================================


def ping_ip(ip):
    result = subprocess.run(f"ping -c 2 {ip}", shell=True)
    return result.returncode == 0


def test_ping_ip(one_device_params):
    assert ping_ip(
        one_device_params["host"]
    ), f"IP адрес {one_device_params['host']} должен пинговаться"


def test_ssh(connect_all):
    result = connect_all.send_command("sh run | i hostname")
    assert "hostname" in result


def test_ospf(connect_all):
    result = connect_all.send_command("sh ip ospf")
    assert "Routing Process" in result, "Должен быть настроен OSPF"


def test_loopback_0(connect_all):
    result = connect_all.send_command("sh ip int br | include up +up")
    assert "Loopback0" in result, "Должен быть настроен Loopback0"
