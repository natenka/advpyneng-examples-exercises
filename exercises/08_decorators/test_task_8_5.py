import time
import pytest
import task_8_5
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_function_exists, check_function_params


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что декоратор создан"""
    check_function_exists(task_8_5, "count_calls")


def test_count_calls_basic(capsys):
    @task_8_5.count_calls
    def do_thing(a, b):
        return a + b

    return_value = do_thing(2, 3)
    # проверка базовой работы функции
    assert return_value == 5

    # на stdout должно выводиться сообщение
    correct_stdout = "всего вызовов: 1"
    out, err = capsys.readouterr()
    assert out != "", "На stdout не выведена информация"
    assert correct_stdout in out.lower(), "На stdout должно выводиться сообщение"


def test_count_calls_repeat(capsys):
    @task_8_5.count_calls
    def do_thing(a, b):
        return a + b

    for _ in range(3):
        do_thing(2, 3)

    # на stdout должно выводиться сообщение
    correct_stdout = "всего вызовов: 3"
    out, err = capsys.readouterr()
    assert out != "", "На stdout не выведена информация"
    assert correct_stdout in out.lower(), "На stdout должно выводиться сообщение"
