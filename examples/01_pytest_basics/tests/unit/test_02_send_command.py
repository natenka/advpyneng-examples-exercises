import pytest
from ex02_send_command_functions import send_show_command
import netmiko


@pytest.mark.parametrize(
    "show_command",
    ["sh ip int br", "sh run"],
)
def test_send_show(cisco_ios_router_reachable, ssh_connection_cisco_ios, show_command):
    correct_output = ssh_connection_cisco_ios.send_command(show_command)
    output = send_show_command(cisco_ios_router_reachable, show_command)
    assert output == correct_output


@pytest.mark.parametrize(
    "host,command",
    [
        ("192.168.100.1", "sh ip int br"),
        ("192.168.100.2", "sh ip int br"),
        ("192.168.100.1", "sh run"),
        ("192.168.100.2", "sh run"),
    ],
)
def test_send_show_reachable(cisco_ios_router_common_params, host, command):
    device = cisco_ios_router_common_params.copy()
    device["host"] = host
    output = send_show_command(device, command)
    assert host in output


@pytest.mark.parametrize("host", ["192.168.100.5", "192.168.100.2", "192.168.100.3"])
def test_send_show_exceptions(cisco_ios_router_common_params, host):
    device = cisco_ios_router_common_params.copy()
    device["host"] = host
    device["password"] = "sdkjfhshdkf"
    with pytest.raises(
        (
            netmiko.ssh_exception.NetmikoTimeoutException,
            netmiko.ssh_exception.NetmikoAuthenticationException,
        )
    ) as exc:
        output = send_show_command(device, "sh ip int br")
