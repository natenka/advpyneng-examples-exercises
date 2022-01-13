import time
import pytest
import task_14_1a
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
    check_function_exists(task_14_1a, "get_intf_ip")


def test_get_intf_ip_is_generator():
    return_value = task_14_1a.get_intf_ip("config_r1.txt")
    assert isinstance(return_value, Generator), "Надо создать генератор"


def test_get_intf_ip_yield_value():
    return_value = task_14_1a.get_intf_ip("config_r1.txt")
    all_results = list(return_value)
    assert (
        "Loopback0",
        "10.1.1.1",
        "255.255.255.255",
    ) in all_results, "Функция вернула неправильный результат"


def test_get_intf_ip_new_file(tmpdir):
    config = (
        "!\n"
        "!\n"
        "interface Loopback0\n"
        " ip address 192.168.10.1 255.255.255.255\n"
        "!\n"
        "interface Ethernet0/1\n"
        " no ip address\n"
        "!\n"
        "interface Ethernet0/2\n"
        " description To P_r9 Ethernet0/2\n"
        " ip address 192.168.20.1 255.255.255.0\n"
        " mpls traffic-eng tunnels\n"
        "!\n"
        "ip access-list standard LDP\n"
        " permit 192.168.20.0 0.0.0.255\n"
        "!\n"
    )
    correct_results = sorted(
        [
            ("Loopback0", "192.168.10.1", "255.255.255.255"),
            ("Ethernet0/2", "192.168.20.1", "255.255.255.0"),
        ]
    )

    # записываем строку config во временный файл
    dest_filename = tmpdir.mkdir("test_tasks").join("task_14_1a.txt")
    dest_filename.write(config)
    # проверяем результат
    return_value = task_14_1a.get_intf_ip(dest_filename)
    assert (
        sorted(return_value) == correct_results
    ), "Функция вернула неправильный результат"
