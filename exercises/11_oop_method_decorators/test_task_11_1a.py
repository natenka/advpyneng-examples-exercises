import pytest
import task_11_1a
import sys

sys.path.append("..")

from common_functions import check_class_exists, check_attr_or_method


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """Проверяем, что класс создан"""
    check_class_exists(task_11_1a, "IPv4Network")


def test_attributes_created():
    """
    Проверяем, что у класса есть метод from_tuple:
    """
    check_attr_or_method(task_11_1a.IPv4Network, method="from_tuple")


def test_create_instance_from_tuple():
    """Проверяем работу объекта"""
    net = task_11_1a.IPv4Network.from_tuple(("100.1.1.0", 25))
    assert isinstance(
        net, task_11_1a.IPv4Network
    ), "Метод from_tuple должен создавать экземпляр класса IPv4Network"
