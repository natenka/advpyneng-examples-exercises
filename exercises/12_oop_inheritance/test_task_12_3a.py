import pytest
import task_12_3a
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_class_exists, check_attr_or_method


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_12_3a, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть атрибут topology"""
    top_with_data = task_12_3a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_sequence_special_methods_created():
    example = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    }
    top = task_12_3a.Topology(example)
    check_attr_or_method(top, method="__getitem__")
    check_attr_or_method(top, method="__setitem__")
    check_attr_or_method(top, method="__delitem__")
    check_attr_or_method(top, method="__len__")
    check_attr_or_method(top, method="__iter__")


def test_sequence_mixin_methods_created():
    example = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    }
    top = task_12_3a.Topology(example)
    check_attr_or_method(top, method="keys")
    check_attr_or_method(top, method="get")
    check_attr_or_method(top, method="pop")
    check_attr_or_method(top, method="clear")
    check_attr_or_method(top, method="update")


def test_method_len():
    example = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }
    top = task_12_3a.Topology(example)
    # test __len__
    assert len(top.topology) == 3


def test_method_getitem():
    example = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }
    top = task_12_3a.Topology(example)

    # test __getitem__
    assert top[("R1", "Eth0/0")] == ("SW1", "Eth0/1")
    assert top[("SW1", "Eth0/1")] == ("R1", "Eth0/0")


def test_method_setitem():
    example = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }
    top = task_12_3a.Topology(example)

    # test __setitem__
    top[("SW1", "Eth0/1")] = ("R1", "Eth0/0")
    assert top[("R1", "Eth0/0")] == ("SW1", "Eth0/1")


def test_method_delitem():
    example = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }
    top = task_12_3a.Topology(example)

    # test __detitem__
    del top[("R1", "Eth0/0")]
    assert len(top.topology) == 2
    # test mirror __detitem__
    del top[("SW1", "Eth0/2")]
    assert len(top.topology) == 1
