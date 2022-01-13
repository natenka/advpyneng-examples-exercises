import pytest
import task_13_1
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """Проверяем, что класс создан и что класс создан с помощью dataclass"""
    check_class_exists(task_13_1, "Route")
    assert hasattr(
        task_13_1.Route, "__dataclass_params__"
    ), "Класс надо создать с помощью dataclass"


def test_attributes_created():
    """
    Проверяем, что у объекта есть атрибуты
    """
    prefix = task_13_1.Route("192.168.1.0/24", "192.168.20.2", "OSPF")
    check_attr_or_method(prefix, attr="prefix")
    check_attr_or_method(prefix, attr="nexthop")
    check_attr_or_method(prefix, attr="protocol")


def test_repr():
    """Проверяем работу repr"""
    prefix = task_13_1.Route("192.168.1.0/24", "192.168.20.2", "OSPF")
    assert "prefix='192.168.1.0/24'" in repr(
        prefix
    ), "Метод repr должен содержать prefix"
    assert "nexthop='192.168.20.2'" in repr(
        prefix
    ), "Метод repr должен содержать nexthop"
    assert "OSPF" not in repr(prefix), "Метод repr НЕ должен содержать protocol"
