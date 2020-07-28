import pytest
import task_7_3
import sys
sys.path.append('..')

from common_functions import check_function_exists, check_function_params, check_attr_or_method


def test_func_created():
    '''Проверяем, что функция создана'''
    check_function_exists(task_7_3, 'queue')


def test_attr_put():
    things = task_7_3.queue()
    check_attr_or_method(things, attr='put')


def test_queue():
    things = task_7_3.queue()
    # put
    things.put(1)
    things.put(2)
    things.put(3)
    # get
    assert things.get() == 1
    assert things.get() == 2
    assert things.get() == 3
    assert things.get() == None

