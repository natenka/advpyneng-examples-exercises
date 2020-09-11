import pytest
import task_13_4
import sys

sys.path.append("..")

from common_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """Проверяем, что класс создан"""
    check_class_exists(task_13_4, "IPv4Network")


def test_attributes_created():
    """
    Проверяем, что у объекта есть атрибуты:
        address, mask, broadcast, allocated, unassigned
    """
    net = task_13_4.IPv4Network("100.7.1.0/26")
    check_attr_or_method(net, attr="network")
    check_attr_or_method(net, attr="broadcast")
    check_attr_or_method(net, attr="allocated")
    check_attr_or_method(net, attr="unassigned")


def test_method_created():
    """
    Проверяем, что у объекта есть метод:
        allocate
    """
    net = task_13_4.IPv4Network("100.7.1.0/26")
    check_attr_or_method(net, method="allocate")


def test_returned_types():
    """Проверяем работу объекта"""
    net = task_13_4.IPv4Network("100.7.1.0/26")
    assert net.allocated == [], "По умолчанию allocated должен содержать пустой список"
    assert isinstance(
        net.unassigned, list
    ), "unassigned должен содержать список IP-адресов"
    assert type(net.hosts) == list, "Метод hosts должен возвращать список"


def test_address_allocation():
    """Проверяем работу объекта"""
    net = task_13_4.IPv4Network("100.7.1.0/26")
    assert len(net.hosts) == 62, "В данной сети должно быть 62 хоста"
    assert net.broadcast == "100.7.1.63", "Broadcast адрес для этой сети 100.7.1.63"

    net.allocate("100.7.1.45")
    net.allocate("100.7.1.15")
    net.allocate("100.7.1.60")

    assert len(net.hosts) == 62, "Метод hosts должен возвращать все хосты"
    assert len(net.allocated) == 3, "Переменная allocated должна содержать 3 хоста"
    assert (
        len(net.unassigned) == 59
    ), "Метод unassigned должен возвращать на 3 хоста меньше"
