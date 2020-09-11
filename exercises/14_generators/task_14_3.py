# -*- coding: utf-8 -*-

"""
Задание 14.3

Создать генератор filter_data_by_attr, который фильтрует данные на основании указанного атрибута и значения.

Аргументы генератора:
* итерируемый объект
* имя атрибута
* значение атрибута

Заменить генераторы filter_by_nexthop и filter_by_mask генератором filter_data_by_attr
в коде ниже. Проверить работу генератора на объектах Route.
Генератор не должен быть привязан к конкретным объектам, то есть должен работать не только
с экземплярами класса Route.

Пример использования функции:

In [1]: import csv
   ...: from collections import namedtuple
   ...:
   ...: f = open('rib_table.csv')
   ...: reader = csv.reader(f)
   ...:
   ...: headers = next(reader)
   ...: Route = namedtuple("Route", headers)
   ...: route_tuples = map(Route._make, reader)
   ...:

In [2]: nhop_23 = filter_data_by_attr(route_tuples, 'nexthop', '200.219.145.23')

In [3]: mask_20 = filter_data_by_attr(nhop_23, 'netmask', '20')

In [4]: next(mask_20)
Out[4]: Route(status='*>', network='23.36.48.0', netmask='20', nexthop='200.219.145.23', metric='NA', locprf='NA', weight='0', path='53242 12956 2914', origin='i')

In [5]: next(mask_20)
Out[5]: Route(status='*>', network='23.36.64.0', netmask='20', nexthop='200.219.145.23', metric='NA', locprf='NA', weight='0', path='53242 12956 1299 20940', origin='i')



"""

import csv
from collections import namedtuple


def filter_by_nexthop(iterable, nexthop):
    for line in iterable:
        if line[3] == nexthop:
            yield line


def filter_by_mask(iterable, mask):
    for line in iterable:
        if line[2] == mask:
            yield line


if __name__ == "__main__":
    with open("rib_table.csv") as f:
        reader = csv.reader(f)
        headers = next(reader)
        Route = namedtuple("Route", headers)
        route_tuples = map(Route._make, reader)

        nhop_23 = filter_by_nexthop(route_tuples, "200.219.145.23")
        mask_20 = filter_by_mask(nhop_23, "20")
