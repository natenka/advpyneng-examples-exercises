# -*- coding: utf-8 -*-
"""
Задание 4.1

Написать тест или тесты для функции generate_access_config. Тест должен проверять:

* тип возвращаемых данных
* наличие команд с настройкой интерфейсов и vlan'ов


Проверить работу функции с разными входящими данными и убедиться, что конфигурация
генерируется правильно.


Тест(ы) написать в файле заданий.
"""

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}


def generate_access_config(intf_vlan_mapping):
    access_mode_template = [
        "switchport mode access",
        "switchport access vlan",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ]
    access_config = []
    for intf, vlan in intf_vlan_mapping.items():
        access_config.append(f"interface {intf}")
        for command in access_mode_template:
            if command.endswith("access vlan"):
                access_config.append(f"{command} {vlan}")
            else:
                access_config.append(command)
    return access_config
