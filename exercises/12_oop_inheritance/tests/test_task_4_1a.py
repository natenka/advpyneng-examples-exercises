import pytest
import task_4_1a
import sys
sys.path.append('..')
from base_telnet_class import TelnetBase

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    '''Проверяем, что класс создан'''
    check_class_exists(task_4_1a, 'CiscoTelnet')


def test_class(first_router_from_devices_yaml):
    '''Проверяем работу объекта'''
    r1 = task_4_1a.CiscoTelnet(**first_router_from_devices_yaml)
    assert isinstance(r1, TelnetBase), "Класс CiscoTelnet должен наследовать TelnetBase"
    check_attr_or_method(r1, method='send_show_command')
    check_attr_or_method(r1, method='send_config_commands')
    with pytest.raises(Exception) as excinfo:
        return_value = r1.send_show_command('sh clck')
    with pytest.raises(Exception) as excinfo:
        return_value = r1.send_config_commands('loggg 7.7.7.7')
    r1._telnet.close()
