import pytest
import task_1_1
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
)


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_init():
    """
    Проверка аннотации в методе __init__
    """
    annotations = task_1_1.IPv4Network.__init__.__annotations__
    assert annotations != {}, "Не написана аннотация для метода __init__"
    assert annotations["return"] == None
    assert annotations["network"] == str


def test_hosts():
    """
    Проверка аннотации в методе hosts
    """
    annotations = task_1_1.IPv4Network.hosts.__annotations__
    assert annotations != {}, "Не написана аннотация для метода __hosts__"
    assert annotations["return"] == list_with_str


def test_repr():
    """
    Проверка аннотации в методе __repr__
    """
    annotations = task_1_1.IPv4Network.__repr__.__annotations__
    assert annotations != {}, "Не написана аннотация для метода __repr__"
    assert annotations["return"] == str


def test_len():
    """
    Проверка аннотации в методе __len__
    """
    annotations = task_1_1.IPv4Network.__len__.__annotations__
    assert annotations != {}, "Не написана аннотация для метода __len__"
    assert annotations["return"] == int


def test_iter():
    """
    Проверка аннотации в методе __iter__
    """
    annotations = task_1_1.IPv4Network.__iter__.__annotations__
    assert annotations != {}, "Не написана аннотация для метода __iter__"
    assert annotations["return"] == iterator_str
