import pytest
import task_6_2
import sys
sys.path.append('..')

from common_functions import check_function_exists, check_function_params


def test_func_created():
    '''Проверяем, что функция создана'''
    check_function_exists(task_6_2, 'count_total')


def test_count_total():
    things = task_6_2.count_total()
    things(15)
    things(5)
    return_value_things = things(35)
    assert return_value_things == 55

    items = task_6_2.count_total()
    items(115)
    items(32)
    return_value_items = items(33)
    assert return_value_items == 180

