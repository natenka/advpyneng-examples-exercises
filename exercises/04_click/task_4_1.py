# -*- coding: utf-8 -*-
"""
Задание 4.1

Создать интерфейс командной строки для скрипта:

* аргумент cdp_filenames, который ожидает один или более файлов с выводом команды sh cdp neighbors
* опция --output-filename, с коротким вариантом -o - CSV файл в который надо записать результат выполнения (обязательное значение)

При запуске скрипта, файлы cdp_filenames и output-filename надо передать как аргументы функции parse_cdp_to_csv,
обработать вывод команды sh cdp neighbors с помощью функции parse_sh_cdp_neighbors и записать результат в csv файл.

Применить декораторы к функции cli!

Help скрипта:

$ python task_4_1.py --help
Usage: task_4_1.py [OPTIONS] CDP_FILENAMES...

Options:
  -o, --output-filename TEXT  [required]
  --help                      Show this message and exit.

Примеры использования скрипта:

$ python task_4_1.py sh_cdp_n_sw1.txt sh_cdp_n_r1.txt -o result.csv
$ python task_4_1.py sh_cdp_n_* -o result.csv
$ python task_4_1.py sh_cdp_n_r[1-4]* -o result.csv

Функции parse_sh_cdp_neighbors и parse_cdp_to_csv менять нельзя.

"""
import csv
import re
from pprint import pprint


def parse_sh_cdp_neighbors(command_output):
    regex = re.compile(
        r"(?P<r_dev>\w+) +(?P<l_intf>\S+ \S+)"
        r" +\d+ +[\w ]+ +\S+ +(?P<r_intf>\S+ \S+)"
    )
    connect_list = []
    match_l_dev = re.search(r"(\S+)[>#]", command_output)
    if match_l_dev:
        l_dev = match_l_dev.group(1)
    for match in regex.finditer(command_output):
        neighbor = (l_dev, *match.group("l_intf", "r_dev", "r_intf"))
        connect_list.append(neighbor)
    return connect_list


def parse_cdp_to_csv(filenames, output_csv):
    with open(output_csv, "w", newline="") as csv_f:
        writer = csv.writer(csv_f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(["local device", "local port", "remote device", "remote port"])
        for filename in filenames:
            with open(filename) as f:
                n_list = parse_sh_cdp_neighbors(f.read())
                writer.writerows(n_list)


# Это просто заготовка, чтобы не забыть, что click надо применять к этой функции
def cli():
    # parse_cdp_to_csv(cdp_filenames, output_filename)
    pass


if __name__ == "__main__":
    cli()
