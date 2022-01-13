import pytest
import task_8_2
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_function_exists, check_function_params


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что декоратор создан"""
    check_function_exists(task_8_2, "all_args_str")


def test_all_args_str():
    @task_8_2.all_args_str
    def do_thing(a, b):
        return f"{a.upper()} {b.upper()}"

    return_value = do_thing("data", "line")
    # проверка базовой работы функции
    assert return_value == "DATA LINE"

    # аргументы не строки, проверка генерации исключения
    error = "все аргументы должны быть строками"
    with pytest.raises(ValueError) as excinfo:
        return_value = do_thing(a=1, b="data")
    assert (
        error in str(excinfo.value).lower()
    ), "Должно генерироваться исключение ValueError с текстом сообщения 'Все аргументы должны быть строками'"
