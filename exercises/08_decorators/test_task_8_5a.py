import time
import pytest
import task_8_5a
import sys

sys.path.append("..")

from advpyneng_helper_functions import (
    check_function_exists,
    check_function_params,
    check_attr_or_method,
)


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что декоратор создан"""
    check_function_exists(task_8_5a, "count_calls")


def test_attr_total_calls_created():
    @task_8_5a.count_calls
    def do_thing(a, b):
        return a + b

    check_attr_or_method(do_thing, attr="total_calls")


def test_count_calls_basic():
    @task_8_5a.count_calls
    def do_thing(a, b):
        return a + b

    return_value = do_thing(2, 3)
    # проверка базовой работы функции
    assert return_value == 5
    assert do_thing.total_calls == 1


def test_count_calls_basic():
    @task_8_5a.count_calls
    def do_thing(a, b):
        return a + b

    for _ in range(3):
        do_thing(2, 3)

    assert do_thing.total_calls == 3
