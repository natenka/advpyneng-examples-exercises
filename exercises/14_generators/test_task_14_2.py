import time
import pytest
import task_14_2
from collections.abc import Generator
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_function_exists, check_function_params

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что функция создана"""
    check_function_exists(task_14_2, "read_file_in_chunks")


def test_read_file_in_chunks_is_generator():
    return_value = task_14_2.read_file_in_chunks("config_r1.txt", 2)
    assert isinstance(return_value, Generator), "Надо создать генератор"


def test_read_file_in_chunks_yield_value():
    return_value = task_14_2.read_file_in_chunks("config_r1.txt", 5)
    first_chunk = next(return_value)
    correct_value = (
        "Current configuration : 4052 bytes\n"
        "!\n"
        "! Last configuration change at 13:13:40 UTC Tue Mar 1 2016\n"
        "version 15.2\n"
        "no service timestamps debug uptime\n"
    )
    assert first_chunk == correct_value, "Функция вернула неправильный результат"


def test_read_file_in_chunks_new_file(tmpdir):
    config1 = (
        "!\n"
        "hostname LONDON-1\n"
        "!\n"
        "interface Loopback0\n"
        " ip address 192.168.10.1 255.255.255.255\n"
        "!\n"
        "interface Ethernet0/2\n"
        " description To P_r9 Ethernet0/2\n"
        " ip address 192.168.20.1 255.255.255.0\n"
        " mpls traffic-eng tunnels\n"
        "!\n"
    )
    correct_value = "!\n" "hostname LONDON-1\n"

    # записываем строки во временный файл
    dest_filename = tmpdir.mkdir("test_tasks").join("task_14_2.txt")
    dest_filename.write(config1)
    # проверяем результат
    return_value = task_14_2.read_file_in_chunks(dest_filename, 2)
    first_chunk = next(return_value)
    assert first_chunk == correct_value, "Функция вернула неправильный результат"

    # проверяем, что получается дочитать файл до конца
    for _ in range(5):
        correct_value += next(return_value)
    assert config1 == correct_value, "Функция вернула неправильный результат"
