import time
import pytest
import task_8_6
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_function_exists, check_function_params


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что декоратор создан"""
    check_function_exists(task_8_6, "total_order")


def test_total_order_exception():
    with pytest.raises(ValueError) as excinfo:
        @task_8_6.total_order
        class DoThing:
            pass


def test_total_order_methods():
    @task_8_6.total_order
    class DoThing:
        def __init__(self, num):
            self.num = num

        def __eq__(self, other):
            return self.num == other.num

        def __lt__(self, other):
            return self.num < other.num

    small_num = DoThing(1)
    big_num = DoThing(100)

    assert small_num < big_num
    assert small_num <= big_num
    assert not small_num > big_num
    assert not small_num >= big_num
    assert small_num != big_num

    small_num = DoThing(1)
    big_num = DoThing(100)

    assert not big_num < small_num
    assert not big_num <= small_num
    assert big_num > small_num
    assert big_num >= small_num
    assert big_num != small_num

    num_1 = DoThing(5)
    num_2 = DoThing(5)

    assert not num_1 < num_2
    assert num_1 <= num_2
    assert not num_1 > num_2
    assert num_1 >= num_2
    assert num_1 == num_2
