import pytest
import task_11_1
import sys

sys.path.append("..")

from common_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """Проверяем, что класс создан"""
    check_class_exists(task_11_1, "IPv4Network")


def test_attributes_created():
    """
    Проверяем, что у объекта есть атрибуты:
        address, mask, broadcast, allocated
    """
    net = task_11_1.IPv4Network("100.7.1.0/26")
    check_attr_or_method(net, attr="address")
    check_attr_or_method(net, attr="mask")
    check_attr_or_method(net, attr="broadcast")
    check_attr_or_method(net, attr="allocated")
    assert (
        net.allocated == tuple()
    ), "По умолчанию allocated должен содержать пустой кортеж"


def test_new_attr_created():
    """
    Проверяем, что у объекта есть переменные:
        allocate, unassigned
    """
    net = task_11_1.IPv4Network("100.7.1.0/26")
    check_attr_or_method(net, method="allocate")
    check_attr_or_method(net, attr="unassigned")
    check_attr_or_method(net, attr="hosts")


def test_return_types():
    """Проверяем работу объекта"""
    net = task_11_1.IPv4Network("100.7.1.0/26")
    assert type(net.hosts) == tuple, "hosts должен возвращать кортеж"
    assert type(net.unassigned) == tuple, "unassigned должен возвращать кортеж"


def test_class():
    """Проверяем работу объекта"""
    net = task_11_1.IPv4Network("100.7.1.0/29")
    assert len(net.hosts) == 6, "В данной сети должно быть 6 хостов"
    assert net.broadcast == "100.7.1.7", "Broadcast адрес для этой сети 100.7.1.7"

    net.allocate("100.7.1.2")
    net.allocate("100.7.1.4")
    net.allocate("100.7.1.5")

    assert len(net.hosts) == 6, "Переменная hosts должна возвращать все хосты"
    assert len(net.allocated) == 3, "Переменная allocated должна содержать 3 хоста"
    assert (
        len(net.unassigned) == 3
    ), "Переменная unassigned должна возвращать на 3 хоста меньше"
    # test net.hosts rewrite
    try:
        net.hosts = "a"
    except AttributeError:
        pass
    else:
        pytest.fail("Запись переменной hosts должна быть запрещена")

    # test net.unassigned rewrite
    try:
        net.unassigned = "a"
    except AttributeError:
        pass
    else:
        pytest.fail("Запись переменной unassigned должна быть запрещена")
