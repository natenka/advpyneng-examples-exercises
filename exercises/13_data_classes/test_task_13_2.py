import pytest
import task_13_2
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """Проверяем, что класс создан и что класс создан с помощью dataclass"""
    check_class_exists(task_13_2, "IPAddress")
    assert hasattr(
        task_13_2.IPAddress, "__dataclass_params__"
    ), "Класс надо создать с помощью dataclass"


def test_method__add__():
    """Проверка наличия метода __add__ и его работы"""

    ip1 = task_13_2.IPAddress("192.168.1.1", 24)
    check_attr_or_method(ip1, method="__add__")
    sum_ip = ip1 + 17

    assert isinstance(
        sum_ip, task_13_2.IPAddress
    ), "Метод __add__ должен возвращать новый экземпляр класса IPAddress"
    assert sum_ip.ip == "192.168.1.18"
