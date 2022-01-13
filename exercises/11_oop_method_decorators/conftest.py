import pytest
import yaml


@pytest.fixture(scope="module")
def first_router_from_devices_yaml():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        r1 = devices[0]
    return r1


@pytest.fixture(scope="module")
def three_routers_from_devices_yaml():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        devices = devices[:3]
    return devices
