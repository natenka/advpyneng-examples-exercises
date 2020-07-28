import pytest
import task_4_5
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


class ForTest(task_4_5.InheritanceMixin):
    pass


def test_class_created():
    check_class_exists(task_4_5, 'InheritanceMixin')


def test_mixin():
    ins = ForTest()
    check_attr_or_method(ins, method='subclasses')
    check_attr_or_method(ins, method='superclasses')
    task_4_5.InheritanceMixin.subclasses()
    task_4_5.InheritanceMixin.superclasses()
    ins.subclasses()
    ins.superclasses()
