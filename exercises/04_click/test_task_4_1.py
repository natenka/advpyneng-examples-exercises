import click
from click.testing import CliRunner
from task_4_1 import cli
import sys

sys.path.append("..")

from advpyneng_helper_functions import read_all_csv_content_as_list

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_cli(tmpdir):
    assert isinstance(
        cli, click.core.Command
    ), "Не настроен click. Декораторы click надо применять к функции cli"
    output_csv = tmpdir.mkdir("test_tasks").join("task_4_1_a.csv")
    runner = CliRunner()
    result = runner.invoke(cli, ["sh_cdp_n_sw1.txt", "-o", output_csv])
    assert (
        result.exit_code == 0
    ), "При передаче одного файла cdp_filenames и одного output-filename cli должно отрабатывать"


def test_cli_wrong_args(tmpdir):
    assert isinstance(
        cli, click.core.Command
    ), "Не настроен click. Декораторы click надо применять к функции cli"
    output_csv = tmpdir.mkdir("test_tasks").join("task_4_1_a.csv")
    runner = CliRunner()
    result = runner.invoke(cli, ["sh_cdp_n_sw1.txt"])
    assert (
        result.exit_code == 2
    ), "--output-filename должен быть обязательным аргументом"


def test_cli_and_file_content(tmpdir):
    correct_return_value = [
        ["local device", "local port", "remote device", "remote port"],
        ["SW1", "Eth 0/1", "R1", "Eth 0/0"],
        ["SW1", "Eth 0/2", "R2", "Eth 0/0"],
        ["SW1", "Eth 0/3", "R3", "Eth 0/0"],
        ["SW1", "Eth 0/4", "R4", "Eth 0/0"],
        ["R1", "Eth 0/0", "SW1", "Eth 0/1"],
    ]

    assert isinstance(
        cli, click.core.Command
    ), "Не настроен click. Декораторы click надо применять к функции cli"
    output_csv = tmpdir.mkdir("test_tasks").join("task_4_1.csv")
    runner = CliRunner()
    result = runner.invoke(
        cli, ["sh_cdp_n_sw1.txt", "sh_cdp_n_r1.txt", "-o", output_csv]
    )
    csv_content = read_all_csv_content_as_list(output_csv)
    assert (
        result.exit_code == 0
    ), "При передаче двух файлов cdp_filenames и одного output-filename cli должно отрабатывать"
    assert sorted(csv_content) == sorted(
        correct_return_value
    ), "Функция возвращает неправильное значение"
