import pytest
import task_5_1
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    '''Проверяем, что класс создан и что класс создан с помощью dataclass'''
    check_class_exists(task_5_1, 'Route')
    assert hasattr(task_5_1.Route, "__dataclass_params__"), "Класс надо создать с помощью dataclass"


def test_attributes_created():
    '''
    Проверяем, что у объекта есть атрибуты
    '''
    prefix = task_5_1.Route('192.168.1.0/24', '192.168.20.2', 'OSPF')
    check_attr_or_method(prefix, attr='prefix')
    check_attr_or_method(prefix, attr='nexthop')
    check_attr_or_method(prefix, attr='protocol')


def test_repr():
    '''Проверяем работу repr'''
    prefix = task_5_1.Route('192.168.1.0/24', '192.168.20.2', 'OSPF')
    assert "prefix='192.168.1.0/24'" in repr(prefix), "Метод repr должен содержать prefix"
    assert "nexthop='192.168.20.2'" in repr(prefix), "Метод repr должен содержать nexthop"
    assert "OSPF" not in repr(prefix), "Метод repr НЕ должен содержать protocol"

