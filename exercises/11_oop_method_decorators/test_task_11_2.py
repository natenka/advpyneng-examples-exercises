import pytest
import task_3_1
import task_3_2
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method, get_reach_unreach


def test_class_created():
    '''Проверяем, что класс создан'''
    check_class_exists(task_3_2, 'PingNetwork')


def test_class():
    '''Проверяем работу объекта'''
    list_of_ips = ['8.8.4.2', '8.8.4.4', '8.8.4.6']
    correct_return_value = get_reach_unreach(list_of_ips)

    net1 = task_3_1.IPv4Network('8.8.4.0/29')
    net1.allocate('8.8.4.2')
    net1.allocate('8.8.4.4')
    net1.allocate('8.8.4.6')

    scan_net = task_3_2.PingNetwork(net1)
    assert scan_net._ping('8.8.4.4') in (True, False), "Метод _ping должен возвращать True или False"
    try:
        task_3_2.PingNetwork._ping('8.8.4.4') in (True, False)
    except TypeError:
        pytest.fail("Метод _ping должен быть статическим")

