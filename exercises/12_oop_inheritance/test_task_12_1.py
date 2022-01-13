import pytest
import task_12_1
import sys

sys.path.append("..")
from base_telnet_class import TelnetBase

from advpyneng_helper_functions import check_class_exists, check_attr_or_method


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """Проверяем, что класс создан"""
    check_class_exists(task_12_1, "CiscoTelnet")


def test_send_config_commands(first_router_from_devices_yaml):
    """Проверяем работу объекта и метода send_config_commands"""
    r1 = task_12_1.CiscoTelnet(**first_router_from_devices_yaml)
    assert isinstance(r1, TelnetBase), "Класс CiscoTelnet должен наследовать TelnetBase"

    # test send_config_commands
    check_attr_or_method(r1, method="send_config_commands")
    cfg_output = r1.send_config_commands(
        ["interface loopback123", "ip address 123.1.2.3 255.255.255.255"]
    )
    assert (
        type(cfg_output) == str
    ), "Метод send_config_commands должен возвращать строку"
    assert (
        "interface loopback123" in cfg_output
        and "ip address 123.1.2.3 255.255.255.255" in cfg_output
    ), "В выводе должны быть строки с командами: 'interface loopback123', 'ip address 123.1.2.3 255.255.255.255'"
    r1.close()


def test_send_show_command(first_router_from_devices_yaml):
    """Проверяем работу метода send_show_command"""
    r1 = task_12_1.CiscoTelnet(**first_router_from_devices_yaml)

    check_attr_or_method(r1, method="send_show_command")
    show_output = r1.send_show_command("sh ip int br")
    assert type(show_output) == str, "Метод send_show_command должен возвращать строку"
    assert (
        "Loopback123" in show_output and "123.1.2.3" in show_output
    ), "В выводе sh ip int br должен быть интерфейс Loopback123 и IP-адрес 123.1.2.3"
    r1.close()
