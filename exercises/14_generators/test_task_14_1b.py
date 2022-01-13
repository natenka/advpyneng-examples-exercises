import time
import pytest
import task_14_1b
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
    check_function_exists(task_14_1b, "get_intf_ip_from_files")


def test_get_intf_ip_from_files_is_generator():
    return_value = task_14_1b.get_intf_ip_from_files("config_r1.txt")
    assert isinstance(return_value, Generator), "Надо создать генератор"


def test_get_intf_ip_from_files_yield_value():
    return_value = task_14_1b.get_intf_ip_from_files("config_r1.txt")
    first_dict = next(return_value)
    assert "PE_r1" in first_dict, "Функция вернула неправильный результат"

    correct_value = {
        "Ethernet0/0": ("10.0.13.1", "255.255.255.0"),
        "Ethernet0/2": ("10.0.19.1", "255.255.255.0"),
        "Loopback0": ("10.1.1.1", "255.255.255.255"),
    }
    assert (
        first_dict["PE_r1"] == correct_value
    ), "Функция вернула неправильный результат"


def test_get_intf_ip_from_files_new_file(tmpdir):
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
    config2 = (
        "hostname LONDON-2\n"
        "!\n"
        "interface Ethernet0/1\n"
        " ip address 10.1.2.1 255.255.255.0\n"
        "!\n"
        "interface Ethernet0/2\n"
        " ip address 10.16.0.1 255.255.255.0\n"
        "!\n"
    )
    correct_results = [
        {
            "LONDON-1": {
                "Loopback0": ("192.168.10.1", "255.255.255.255"),
                "Ethernet0/2": ("192.168.20.1", "255.255.255.0"),
            }
        },
        {
            "LONDON-2": {
                "Ethernet0/1": ("10.1.2.1", "255.255.255.0"),
                "Ethernet0/2": ("10.16.0.1", "255.255.255.0"),
            }
        },
    ]

    # записываем строки во временные файлы
    temp_dir = tmpdir.mkdir("test_tasks")
    dest_filename1 = temp_dir.join("task_14_1b_1.txt")
    dest_filename1.write(config1)
    dest_filename2 = temp_dir.join("task_14_1b_2.txt")
    dest_filename2.write(config2)
    # проверяем результат
    return_value = task_14_1b.get_intf_ip_from_files(dest_filename1, dest_filename2)
    assert (
        list(return_value) == correct_results
    ), "Функция вернула неправильный результат"
