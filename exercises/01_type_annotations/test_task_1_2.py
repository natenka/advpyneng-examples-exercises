import pytest
import task_1_2
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
)


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_send_show_return():
    """
    Проверка аннотации возвращаемого значения
    """
    annotations = task_1_2.send_show.__annotations__
    assert annotations != {}, "Не написана аннотация для функции send_show"
    assert annotations["return"] == str


def test_send_show_params():
    """
    Проверка аннотации параметров
    """
    annotations = task_1_2.send_show.__annotations__
    assert annotations != {}, "Не написана аннотация для функции send_show"
    assert annotations["command"] == str
    assert (
        annotations["device_dict"] == dict_with_str
        or annotations["device_dict"] == dict_with_str_any
    )


def test_send_command_to_devices_return():
    """
    Проверка аннотации возвращаемого значения
    """
    annotations = task_1_2.send_command_to_devices.__annotations__
    assert (
        annotations != {}
    ), "Не написана аннотация для функции send_command_to_devices"
    assert annotations["return"] == dict_with_str


def test_send_command_to_devices_params():
    """
    Проверка аннотации параметров
    """
    annotations = task_1_2.send_command_to_devices.__annotations__
    assert annotations["command"] == str
    assert annotations["max_workers"] == int
    assert annotations["devices"] == list_of_dicts_with_str
