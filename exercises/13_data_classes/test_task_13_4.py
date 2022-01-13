import pytest
import task_13_4
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_class_exists, check_attr_or_method

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
    check_attr_or_method(net, method="allocate_ip")
    check_attr_or_method(net, method="free_ip")


@pytest.mark.parametrize(
    "attr_name,attr_type",
    [
        ("network", str),
        ("broadcast", str),
        ("hosts", tuple),
        ("unassigned", set),
        ("allocated", set),
    ],
)
def test_return_types(attr_name, attr_type):
    """Проверяем типы"""
    net = task_13_4.IPv4Network("100.7.1.0/26")
    attr_value = getattr(net, attr_name)
    assert type(attr_value) == attr_type, (
        f"По заданию в атрибуте {attr_name} должно быть значение типа {attr_type},"
        f" а в нем {type(attr_value).__name__}"
    )


def test_address_allocation():
    """Проверяем работу объекта"""
    net = task_13_4.IPv4Network("100.7.1.0/26")
    assert len(net.hosts) == 62, "В данной сети должно быть 62 хоста"
    assert net.broadcast == "100.7.1.63", "Broadcast адрес для этой сети 100.7.1.63"

    net.allocate_ip("100.7.1.45")
    net.allocate_ip("100.7.1.15")
    net.allocate_ip("100.7.1.60")

    assert len(net.hosts) == 62, "Метод hosts должен возвращать все хосты"
    assert len(net.allocated) == 3, "Переменная allocated должна содержать 3 хоста"
    assert (
        len(net.unassigned) == 59
    ), "Метод unassigned должен возвращать на 3 хоста меньше"


def test_address_allocation_with_gw():
    """Проверяем работу объекта"""
    net = task_13_4.IPv4Network("100.7.1.0/26", gw="100.7.1.1")
    net.allocate_ip("100.7.1.45")
    net.allocate_ip("100.7.1.15")
    net.allocate_ip("100.7.1.60")

    assert len(net.hosts) == 62, "Метод hosts должен возвращать все хосты"
    assert len(net.allocated) == 4, "Переменная allocated должна содержать 4 хоста"
    assert (
        len(net.unassigned) == 58
    ), "Переменная unassigned должна возвращать на 4 хоста меньше, чем hosts"

    net.free_ip("100.7.1.45")
    net.free_ip("100.7.1.60")
    assert len(net.allocated) == 2, "Переменная allocated должна содержать 2 хоста"
    assert (
        len(net.unassigned) == 60
    ), "Переменная unassigned должна возвращать на 2 хоста меньше, чем hosts"


def test_exceptions():
    """Проверяем работу объекта"""
    net = task_13_4.IPv4Network("100.7.1.0/26", gw="100.7.1.1")
    net.allocate_ip("100.7.1.45")
    with pytest.raises(ValueError):
        # allocate_ip тот же адрес второй раз
        net.allocate_ip("100.7.1.45")
    with pytest.raises(ValueError):
        # адрес не из сети 100.7.1.0/26
        net.allocate_ip("100.7.1.253")
    net.free_ip("100.7.1.45")
    with pytest.raises(ValueError):
        # free_ip тот же адрес второй раз
        net.free_ip("100.7.1.45")
