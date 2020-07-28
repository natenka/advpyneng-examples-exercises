import pytest
import task_5_2
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    '''Проверяем, что класс создан и что класс создан с помощью dataclass'''
    check_class_exists(task_5_2, 'IPAddress')
    assert hasattr(task_5_2.IPAddress, "__dataclass_params__"), "Класс надо создать с помощью dataclass"


def test_method__add__():
    '''Проверка наличия метода __add__ и его работы'''

    ip1 = task_5_2.IPAddress('192.168.1.1', 24)
    check_attr_or_method(ip1, method='__add__')
    sum_ip = ip1 + 17

    assert isinstance(sum_ip, task_5_2.IPAddress), "Метод __add__ должен возвращать новый экземпляр класса IPAddress"
    assert sum_ip.ip == '192.168.1.18'
