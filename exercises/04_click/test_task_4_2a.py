import click
from click.testing import CliRunner
from task_4_2a import cli
import sys

sys.path.append("..")

from advpyneng_helper_functions import read_all_csv_content_as_list

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_cli(first_router_from_devices_yaml):
    ip = first_router_from_devices_yaml["ip"]
    username = first_router_from_devices_yaml["username"]
    password = first_router_from_devices_yaml["password"]
    enable_password = first_router_from_devices_yaml["enable_password"]

    assert isinstance(
        cli, click.core.Command
    ), "Не настроен click. Декораторы click надо применять к функции cli"
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ["sh clock", ip, "-u", username, "-p", password, "-s", enable_password],
    )
    assert (
        result.exit_code == 0
    ), f'CLI не отработал с таким вызовом python task_4_2a.py "sh clock" {ip} -u {username} -p {password} -s {enable_password}'


def test_cli_input_enable_password(first_router_from_devices_yaml):
    ip = first_router_from_devices_yaml["ip"]
    username = first_router_from_devices_yaml["username"]
    password = first_router_from_devices_yaml["password"]
    enable_password = first_router_from_devices_yaml["enable_password"]

    assert isinstance(
        cli, click.core.Command
    ), "Не настроен click. Декораторы click надо применять к функции cli"
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ["sh clock", ip, "-u", username, "-p", password],
        input=enable_password,
    )
    assert (
        result.exit_code == 0
    ), f'CLI не отработал с таким вызовом python task_4_2a.py "sh clock" {ip} -u {username} -p {password}'


def test_cli_input_username(first_router_from_devices_yaml):
    ip = first_router_from_devices_yaml["ip"]
    username = first_router_from_devices_yaml["username"]
    password = first_router_from_devices_yaml["password"]
    enable_password = first_router_from_devices_yaml["enable_password"]

    assert isinstance(
        cli, click.core.Command
    ), "Не настроен click. Декораторы click надо применять к функции cli"
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ["sh clock", ip, "-p", password, "-s", enable_password],
        input=username,
    )
    assert (
        result.exit_code == 0
    ), f'CLI не отработал с таким вызовом python task_4_2a.py "sh clock" {ip} -u {username} -p {password}'
