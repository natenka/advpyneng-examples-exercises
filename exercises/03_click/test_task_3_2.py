from click.testing import CliRunner
from task_3_2 import cli
import sys

sys.path.append("..")

from common_functions import read_all_csv_content_as_list

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["sh clock", "-y", "devices.yaml", "-t", "3"])
    assert (
        result.exit_code == 0
    ), 'CLI не отработал с таким вызовом python task_3_2.py "sh clock" -y devices.yaml -t 3'


def test_cli_threads():
    runner = CliRunner()
    result = runner.invoke(cli, ["sh clock", "-y", "devices.yaml"])
    assert (
        result.exit_code == 0
    ), 'CLI не отработал с таким вызовом python task_3_2.py "sh clock" -y devices.yaml. У threads должно быть значение по умолчанию = 5'


def test_cli_threads_max():
    runner = CliRunner()
    result = runner.invoke(cli, ["sh clock", "-y", "devices.yaml", "-t", "15"])
    assert result.exit_code == 2, "Максимальное значение threads должно быть 10"
