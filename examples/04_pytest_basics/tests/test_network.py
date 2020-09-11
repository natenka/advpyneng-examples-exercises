import pytest
import subprocess


def ping_ip(ip):
    result = subprocess.run(f"ping -c 2 {ip}", shell=True)
    return result.returncode == 0


@pytest.mark.parametrize("ip", ["192.168.100.1", "192.168.100.2", "192.168.100.3"])
def test_ip(ip):
    assert ping_ip(ip)
