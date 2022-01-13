import pytest
import task_2_1
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
)


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_init():
    """
    Проверка аннотации в методе __init__
    """
    annotations = task_2_1.IPv4Network.__init__.__annotations__
    assert annotations != {}, "Не написана аннотация для метода __init__"
    assert (
        annotations.get("return", False) != False
    ), "Не написана аннотация для того, что возвращается в методе __init__"
    assert annotations.get("return") == None
    assert annotations.get("network") == str


def test_hosts():
    """
    Проверка аннотации в методе hosts
    """
    annotations = task_2_1.IPv4Network.hosts.__annotations__
    assert annotations != {}, "Не написана аннотация для метода hosts"
    assert (
        annotations.get("return", False) != False
    ), "Не написана аннотация для того, что возвращается в методе hosts"
    assert annotations["return"] == list_with_str or annotations["return"] == list[str]


def test_repr():
    """
    Проверка аннотации в методе __repr__
    """
    annotations = task_2_1.IPv4Network.__repr__.__annotations__
    assert annotations != {}, "Не написана аннотация для метода __repr__"
    assert (
        annotations.get("return", False) != False
    ), "Не написана аннотация для того, что возвращается в методе __repr__"
    assert annotations["return"] == str


def test_len():
    """
    Проверка аннотации в методе __len__
    """
    annotations = task_2_1.IPv4Network.__len__.__annotations__
    assert annotations != {}, "Не написана аннотация для метода __len__"
    assert (
        annotations.get("return", False) != False
    ), "Не написана аннотация для того, что возвращается в методе __len__"
    assert annotations["return"] == int


def test_iter():
    """
    Проверка аннотации в методе __iter__
    """
    annotations = task_2_1.IPv4Network.__iter__.__annotations__
    assert annotations != {}, "Не написана аннотация для метода __iter__"
    assert (
        annotations.get("return", False) != False
    ), "Не написана аннотация для того, что возвращается в методе __iter__"
    assert annotations["return"] == iterator_str
