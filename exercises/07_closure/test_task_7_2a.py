import pytest
import task_6_2a
import sys
sys.path.append('..')

from common_functions import check_function_exists, check_function_params, check_attr_or_method


def test_func_created():
    '''Проверяем, что функция создана'''
    check_function_exists(task_6_2a, 'count_total')


def test_attr_buy():
    things = task_6_2a.count_total()
    check_attr_or_method(things, attr='buy')


def test_count_total():
    things = task_6_2a.count_total()
    things.buy(15)
    things.buy(5)
    return_value_things = things.buy(35)
    assert return_value_things == 55

    items = task_6_2a.count_total()
    items.buy(115)
    items.buy(32)
    return_value_items = items.buy(33)
    assert return_value_items == 180

