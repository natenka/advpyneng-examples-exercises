import pytest
import task_6_1
import sys
sys.path.append('..')

from common_functions import check_function_exists, check_function_params


def test_func_created():
    '''Проверяем, что функция создана'''
    check_function_exists(task_6_1, 'netmiko_ssh')


def test_netmiko_ssh(capsys):
    r1 = task_6_1.netmiko_ssh(**task_6_1.device_params)
    # проверка отправки команды и вывода
    assert task_6_1.device_params['ip'] in r1('sh ip int br')

    # при закрытии сессии на stdout должно выводиться сообщение
    r1('close')
    correct_stdout = 'Соединение закрыто'
    out, err = capsys.readouterr()
    assert out != '', "Сообщение об ошибке не выведено на stdout"
    assert correct_stdout in out, "Выведено неправильное сообщение об ошибке"
