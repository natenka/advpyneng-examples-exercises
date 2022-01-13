import pytest
import task_2_3
from collections.abc import MutableMapping
import sys

sys.path.append("..")

from advpyneng_helper_functions import (
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
    annotations = task_2_3.Topology.__init__.__annotations__
    assert annotations != {}, "Не написана аннотация для метода __init__"
    assert (
        annotations.get("return", False) != False
    ), "Не написана аннотация для того, что возвращается в методе __init__"
    assert annotations["return"] == None
    assert (
        annotations.get("topology_dict") == dict_tuple
        or annotations.get("topology_dict") == dict[tuple[str, str], tuple[str, str]]
    )


def test__normalize():
    """
    Проверка аннотации в методе _normalize
    """
    annotations = task_2_3.Topology._normalize.__annotations__
    assert annotations != {}, "Не написана аннотация для метода _normalize"
    assert (
        annotations.get("return", False) != False
    ), "Не написана аннотация для того, что возвращается в методе _normalize"
    assert (
        annotations["return"] == dict_tuple
        or annotations["return"] == dict[tuple[str, str], tuple[str, str]]
    )
    assert (
        annotations.get("topology_dict") == dict_tuple
        or annotations.get("topology_dict") == dict[tuple[str, str], tuple[str, str]]
    )


def test_delete_link():
    """
    Проверка аннотации в методе delete_link
    """
    annotations = task_2_3.Topology.delete_link.__annotations__
    assert annotations != {}, "Не написана аннотация для метода delete_link"
    assert (
        annotations.get("return", False) != False
    ), "Не написана аннотация для того, что возвращается в методе delete_link"
    assert annotations["return"] == None
    assert (
        annotations.get("from_port") == tuple_two_str
        or annotations.get("from_port") == tuple[str, str]
    )
    assert (
        annotations.get("to_port") == tuple_two_str
        or annotations.get("to_port") == tuple[str, str]
    )
