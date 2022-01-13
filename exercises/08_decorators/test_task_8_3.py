import time
import pytest
import task_8_3
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_function_exists, check_function_params


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что декоратор создан"""
    check_function_exists(task_8_3, "add_verbose")


def test_add_verbose(capsys):
    @task_8_3.add_verbose
    def do_thing(a, b):
        return a + b

    return_value = do_thing(2, 3)
    # проверка базовой работы функции
    assert return_value == 5


def test_add_verbose_args(capsys):
    @task_8_3.add_verbose
    def do_thing(a, b):
        return a + b

    # должно выводиться сообщение
    return_value = do_thing(2, 3, verbose=True)
    correct_stdout = "позиционные аргументы"
    out, err = capsys.readouterr()
    assert out != "", "На stdout не выведена информация"
    assert (
        correct_stdout in out.lower()
    ), "На stdout не выведена информация про аргументы функции"


def test_add_verbose_kwargs(capsys):
    @task_8_3.add_verbose
    def do_thing(a, b):
        return a + b

    # должно выводиться сообщение
    return_value = do_thing(a=2, b=3, verbose=True)
    correct_stdout = "ключевые аргументы"
    out, err = capsys.readouterr()
    assert out != "", "На stdout не выведена информация"
    assert (
        correct_stdout in out.lower()
    ), "На stdout не выведена информация про аргументы функции"


def test_add_verbose_args_kwargs(capsys):
    @task_8_3.add_verbose
    def do_thing(a, b):
        return a + b

    # должно выводиться сообщение
    return_value = do_thing(2, b=3, verbose=True)
    out, err = capsys.readouterr()
    assert out != "", "На stdout не выведена информация"
    assert (
        "позиционные аргументы" in out.lower() and "ключевые аргументы" in out.lower()
    ), "На stdout не выведена информация про аргументы функции"
