import time
import pytest
import task_14_3
from collections.abc import Generator
from collections import namedtuple
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_function_exists, check_function_params


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что функция создана"""
    check_function_exists(task_14_3, "filter_data_by_attr")


def test_filter_data_by_attr_is_generator():
    Book = namedtuple("Book", "title author")
    books = [
        Book(title="1984", author="George Orwell"),
        Book(title="Animal Farm", author="George Orwell"),
        Book(title="To Kill a Mockingbird", author="Harper Lee"),
    ]

    return_value = task_14_3.filter_data_by_attr(books, "author", "George Orwell")
    assert isinstance(return_value, Generator), "Надо создать генератор"


def test_filter_data_by_attr_yield_value():
    Book = namedtuple("Book", "title author")
    books = [
        Book(title="1984", author="George Orwell"),
        Book(title="The Martian Chronicles", author="Ray Bradbury"),
        Book(title="The Hobbit", author="J.R.R. Tolkien"),
        Book(title="Animal Farm", author="George Orwell"),
        Book(title="Fahrenheit 451", author="Ray Bradbury"),
        Book(title="The Lord of the Rings (1-3)", author="J.R.R. Tolkien"),
        Book(title="Harry Potter and the Sorcerer’s Stone", author="J.K. Rowling"),
        Book(title="To Kill a Mockingbird", author="Harper Lee"),
    ]

    return_value = task_14_3.filter_data_by_attr(books, "author", "George Orwell")
    orwell = list(return_value)
    correct_value = [
        Book(title="1984", author="George Orwell"),
        Book(title="Animal Farm", author="George Orwell"),
    ]
    assert orwell == correct_value, "Функция вернула неправильный результат"
