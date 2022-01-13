import pytest
import task_7_1
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_function_exists, check_function_params

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что функция создана"""
    check_function_exists(task_7_1, "netmiko_ssh")


def test_netmiko_ssh(capsys):
    r1 = task_7_1.netmiko_ssh(**task_7_1.device_params)
    # проверка отправки команды и вывода
    assert task_7_1.device_params["ip"] in r1("sh ip int br")

    # при закрытии сессии на stdout должно выводиться сообщение
    r1("close")
    correct_stdout = "соединение закрыто"
    out, err = capsys.readouterr()
    assert out != "", "Сообщение об ошибке не выведено на stdout"
    assert correct_stdout in out.lower(), "Выведено неправильное сообщение об ошибке"
