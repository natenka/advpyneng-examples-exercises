import pytest
import task_2_1
import task_2_2
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method, get_reach_unreach


def test_class_created():
    '''Проверяем, что класс создан'''
    check_class_exists(task_2_2, 'PingNetwork')


def test_class():
    '''Проверяем работу объекта'''
    list_of_ips = ['8.8.4.2', '8.8.4.4', '8.8.4.6']
    correct_return_value = get_reach_unreach(list_of_ips)

    net1 = task_2_1.IPv4Network('8.8.4.0/29')
    net1.allocate('8.8.4.2')
    net1.allocate('8.8.4.4')
    net1.allocate('8.8.4.6')

    scan_net = task_2_2.PingNetwork(net1)
    assert callable(scan_net) == True
    return_value = scan_net()
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == tuple and all(type(item)==list for item in return_value), "Метод scan должен возвращать кортеж с двумя списками"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"
    # include_unassigned = True
    assert type(scan_net(include_unassigned=True)) == tuple
