import pytest
import task_12_4
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_class_exists, check_attr_or_method


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_12_4, "OrderingMixin")


def test_special_methods_created():
    class IntTest(task_12_4.OrderingMixin):
        def __init__(self, number):
            self._number = number

        def __eq__(self, other):
            return self._number == other._number

        def __lt__(self, other):
            return self._number < other._number

    int1 = IntTest(5)
    check_attr_or_method(int1, method="__ge__")
    check_attr_or_method(int1, method="__ne__")
    check_attr_or_method(int1, method="__le__")
    check_attr_or_method(int1, method="__gt__")


def test_methods():
    class IntTest(task_12_4.OrderingMixin):
        def __init__(self, number):
            self._number = number

        def __eq__(self, other):
            return self._number == other._number

        def __lt__(self, other):
            return self._number < other._number

    int1 = IntTest(5)
    int2 = IntTest(3)

    assert int1 != int2
    assert int1 >= int2
    assert int1 > int2
    assert not int1 < int2


def test_methods():
    class DoThing(task_12_4.OrderingMixin):
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

    num_1 = DoThing(10)
    num_2 = DoThing(10)

    assert not num_1 < num_2
    assert num_1 <= num_2
    assert not num_1 > num_2
    assert num_1 >= num_2
    assert num_1 == num_2
