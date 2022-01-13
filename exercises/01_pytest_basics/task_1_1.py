# -*- coding: utf-8 -*-
"""
Задание 1.1

Написать тест или тесты для функции get_int_vlan_map. Тест должен проверять:

* тип возвращаемых данных
* что словари, которые возвращает функция, содержат правильные данные

Проверить работу функции с разными входящими данными и убедиться, что словари
генерируются правильно для этих данных.
Пример вызова функции показан в файле заданий.

Тест(ы) написать в файле заданий.

Ограничение: функцию менять нельзя.
Для заданий этого раздела нет тестов для проверки тестов :)
"""
from pprint import pprint


def get_int_vlan_map(config_as_str):
    access_port_dict = {}
    trunk_port_dict = {}
    for line in config_as_str.splitlines():
        if line.startswith("interface") and "Ethernet" in line:
            current_interface = line.split()[-1]
            access_port_dict[current_interface] = 1
        elif "switchport access vlan" in line:
            access_port_dict[current_interface] = int(line.split()[-1])
        elif "switchport trunk allowed vlan" in line:
            vlans = [int(i) for i in line.split()[-1].split(",")]
            trunk_port_dict[current_interface] = vlans
            del access_port_dict[current_interface]
    return access_port_dict, trunk_port_dict


if __name__ == "__main__":
    with open("config_sw1.txt") as f:
        pprint(get_int_vlan_map(f.read()))
    with open("config_sw2.txt") as f:
        pprint(get_int_vlan_map(f.read()))
