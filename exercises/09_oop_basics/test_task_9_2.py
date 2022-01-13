import pytest
import task_9_1
import task_9_2
import sys

sys.path.append("..")

from advpyneng_helper_functions import (
    check_class_exists,
    check_attr_or_method,
    get_reach_unreach,
)


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """Проверяем, что класс создан"""
    check_class_exists(task_9_2, "PingNetwork")


def test_methods_created():
    """
    Проверяем, что у объекта есть методы:
        _ping, scan
    """
    scan_net = task_9_2.PingNetwork(task_9_1.IPv4Network("8.8.4.0/29"))
    check_attr_or_method(scan_net, method="_ping")
    check_attr_or_method(scan_net, method="scan")


def test_class():
    """Проверяем работу объекта"""
    list_of_ips = ["8.8.4.2", "8.8.4.4", "8.8.4.6"]
    correct_return_value = get_reach_unreach(list_of_ips)

    net1 = task_9_1.IPv4Network("8.8.4.0/29")
    net1.allocate_ip("8.8.4.2")
    net1.allocate_ip("8.8.4.4")
    net1.allocate_ip("8.8.4.6")

    scan_net = task_9_2.PingNetwork(net1)
    assert scan_net._ping("8.8.4.4") in (
        True,
        False,
    ), "Метод _ping должен возвращать True или False"
    return_value = scan_net.scan()
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == tuple and all(
        type(item) == list for item in return_value
    ), "Метод scan должен возвращать кортеж с двумя списками"
    reach, unreach = return_value
    assert (
        (sorted(reach), sorted(unreach)) == correct_return_value
    ), "Функция возвращает неправильное значение"
