import re
import time
import random
import pytest
import task_11_3
import sys

sys.path.append("..")

from advpyneng_helper_functions import (
    check_attr_or_method,
)


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def get_random_loop_number(cfg):
    loop_int_numbers = re.findall(r"interface Loopback(\d+)", cfg)
    if loop_int_numbers:
        max_num = max(map(int, loop_int_numbers))
    else:
        max_num = 0

    create_loop = max_num + random.choice(range(200, 300))
    return create_loop


def test_cfg(first_router_from_devices_yaml):
    r1 = task_11_3.CiscoTelnet(**first_router_from_devices_yaml, config_cache_timeout=3)
    check_attr_or_method(r1, attr="cfg")
    # get config to check Loopback interfaces
    config = r1.send_show_command("sh run")
    loop_num = get_random_loop_number(config)
    loop_intf = f"Loopback{loop_num}"

    # get cfg
    r1.cfg
    # create interface
    r1.send_config(f"interface {loop_intf}")
    assert (
        loop_intf not in r1.cfg
    ), "r1.cfg выполнено сразу после команды, должен отдаваться кеш"
    time.sleep(5)
    assert (
        loop_intf in r1.cfg
    ), "r1.cfg выполнено после паузы > config_cache_timeout, конфиг должен быть считан заново"
