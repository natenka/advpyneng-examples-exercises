import pytest
import task_12_5
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


class ForTest(task_12_5.InheritanceMixin):
    pass


def test_class_created():
    check_class_exists(task_12_5, "InheritanceMixin")


def test_mixin():
    ins = ForTest()
    check_attr_or_method(ins, method="subclasses")
    check_attr_or_method(ins, method="superclasses")
    task_12_5.InheritanceMixin.subclasses()
    task_12_5.InheritanceMixin.superclasses()
    ins.subclasses()
    ins.superclasses()
