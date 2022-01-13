import re
import time
import random
import pytest
import task_11_5
import sys

sys.path.append("..")

from advpyneng_helper_functions import (
    check_attr_or_method,
)


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_password(first_router_from_devices_yaml, monkeypatch):
    password = first_router_from_devices_yaml.pop("password")
    monkeypatch.setattr("builtins.input", lambda x=None: password)
    check_attr_or_method(task_11_5.CiscoTelnet, method="input_params")
    r1 = task_11_5.CiscoTelnet.input_params(**first_router_from_devices_yaml)
    # если в предыдущей строке все правильно с подключением, команда sh clock
    # должна выполниться без исключений
    output = r1.send_show_command("sh clock")
    assert "sh clock" in output


def test_username(first_router_from_devices_yaml, monkeypatch):
    username = first_router_from_devices_yaml.pop("username")
    monkeypatch.setattr("builtins.input", lambda x=None: username)
    check_attr_or_method(task_11_5.CiscoTelnet, method="input_params")
    r1 = task_11_5.CiscoTelnet.input_params(**first_router_from_devices_yaml)
    # если в предыдущей строке все правильно с подключением, команда sh clock
    # должна выполниться без исключений
    output = r1.send_show_command("sh clock")
    assert "sh clock" in output
