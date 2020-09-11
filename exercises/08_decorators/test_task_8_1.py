import time
import pytest
import task_8_1
import sys

sys.path.append("..")

from common_functions import check_function_exists, check_function_params

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что декоратор и функция send_show_command созданы"""
    check_function_exists(task_8_1, "timecode")
    check_function_exists(task_8_1, "send_show_command")


def test_timecode(capsys):
    @task_8_1.timecode
    def do_thing(a, b):
        time.sleep(2)
        return a + b

    return_value = do_thing(2, 3)
    # проверка базовой работы функции
    assert return_value == 5

    # должно выводиться сообщение со временем выполнения
    correct_stdout = "Функция выполнялась"
    out, err = capsys.readouterr()
    seconds = float(out.strip().split(":")[-1])
    assert out != "", "Сообщение об ошибке не выведено на stdout"
    assert correct_stdout in out, "Выведено неправильное сообщение об ошибке"
    assert 1 < seconds < 4
