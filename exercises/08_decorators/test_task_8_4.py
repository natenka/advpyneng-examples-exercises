import time
import pytest
import task_8_4
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_function_exists, check_function_params


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что декоратор создан"""
    check_function_exists(task_8_4, "retry")


def test_retry_success(capsys):
    @task_8_4.retry(3)
    def do_thing(a, b):
        print("done")
        return a + b

    return_value = do_thing(2, 3)
    # проверка базовой работы функции
    assert return_value == 5

    # должно выводиться сообщение со временем выполнения
    correct_stdout = "done"
    out, err = capsys.readouterr()
    assert out != "", "На stdout не выведена информация"
    assert correct_stdout in out, "На stdout должно выводиться сообщение"


def test_retry_failed(capsys):
    @task_8_4.retry(2)
    def do_thing(a, b):
        print("done")
        return None

    return_value = do_thing(2, 3)

    # должно выводиться сообщение со временем выполнения
    correct_stdout = "done"
    out, err = capsys.readouterr()
    assert out != "", "На stdout не выведена информация"
    assert (
        out.count(correct_stdout) == 3
    ), "При каждом выполнении функции на stdout должно выводиться сообщение"
