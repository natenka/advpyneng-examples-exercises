import pytest
import task_12_1a
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
    check_class_exists(task_12_1a, "CiscoTelnet")


def test_class(first_router_from_devices_yaml):
    """Проверяем работу объекта"""
    r1 = task_12_1a.CiscoTelnet(**first_router_from_devices_yaml)
    assert isinstance(r1, TelnetBase), "Класс CiscoTelnet должен наследовать TelnetBase"
    check_attr_or_method(r1, method="send_show_command")
    check_attr_or_method(r1, method="send_config_commands")
    with pytest.raises(Exception) as excinfo:
        return_value = r1.send_show_command("sh clck")
    with pytest.raises(Exception) as excinfo:
        return_value = r1.send_config_commands("loggg 7.7.7.7")
    r1._telnet.close()
