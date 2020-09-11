import pytest
import task_1_3
from collections.abc import MutableMapping
import sys

sys.path.append("..")

from common_functions import (
    check_function_exists,
    check_function_params,
    dict_with_str,
    list_with_str,
    list_of_dicts_with_str,
    dict_with_str_any,
    iterator_str,
    dict_tuple,
    tuple_two_str,
)


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_init():
    """
    Проверка аннотации в методе __init__
    """
    annotations = task_1_3.Topology.__init__.__annotations__
    assert annotations != {}, "Не написана аннотация для метода __init__"
    assert annotations["return"] == None
    assert annotations["topology_dict"] == dict_tuple


def test__normalize():
    """
    Проверка аннотации в методе _normalize
    """
    annotations = task_1_3.Topology._normalize.__annotations__
    assert annotations != {}, "Не написана аннотация для метода ___normalize__"
    assert annotations["return"] == dict_tuple
    assert annotations["topology_dict"] == dict_tuple


def test_delete_link():
    """
    Проверка аннотации в методе delete_link
    """
    annotations = task_1_3.Topology.delete_link.__annotations__
    assert annotations != {}, "Не написана аннотация для метода delete_link"
    assert annotations["return"] == None
    assert annotations["from_port"] == tuple_two_str
    assert annotations["to_port"] == tuple_two_str
