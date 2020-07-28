# -*- coding: utf-8 -*-
'''
Задание 18.3

Создать сопрограмму (coroutine) get_all_cdp_neighbors. Сопрограмма
ожидает как аргумент список файлов с выводом sh cdp neighbors detail и парсит
файлы параллельно.

В задании скопирован код функций:

* get_one_neighbor - возвращает по одному соседу из файла с выводом sh cdp neighbors detail
* parse_neighbor - парсит одного соседа и возвращает словарь

Эти функции можно использовать для решения и можно менять.

Функция должна возвращать список словарей в таком формате:

[{'sw1': {'R1': {'ios': '12.4(24)T1', 'ip': '10.1.1.1', 'platform': 'Cisco 3825'},
          'R2': {'ios': '15.2(2)T1', 'ip': '10.2.2.2', 'platform': 'Cisco 2911'},
          'R3': {'ios': '15.2(2)T1', 'ip': '10.3.3.3', 'platform': 'Cisco 2911'},
          'SW2': {'ios': '12.2(55)SE9', 'ip': '10.1.1.2', 'platform': 'cisco WS-C2960-8TC-L'}}},
 {'r1': {'R4': {'ios': '15.2(2)T1', 'ip': '10.4.4.4', 'platform': 'Cisco 2911'},
         'SW1': {'ios': '12.2(55)SE9', 'ip': '10.1.1.100', 'platform': 'cisco WS-C2960-8TC-L'}}}]

Имя устройства надо получить из имени файла, остальное из вывода команды.

Запустить сопрограмму и проверить, что она работает корректно с файлами
sh_cdp_neighbors_detail_sw1.txt, sh_cdp_neighbors_detail_r1.txt

При необходимости, можно использовать функции из предыдущих заданий
и создавать дополнительные функции.
Для заданий в этом разделе нет тестов!

'''
import re
from pprint import pprint
import asyncio

import aiofiles


async def get_one_neighbor(filename):
    async with aiofiles.open(filename) as f:
        line = ''
        while True:
            while not 'Device ID' in line:
                line = await f.readline()
            neighbor = line
            async for line in f:
                if '----------' in line:
                    break
                neighbor += line
            yield neighbor
            line = await f.readline()
            if not line:
                return


def parse_neighbor(output):
    regex = (
        r'Device ID: (\S+).+?'
        r' IP address: (?P<ip>\S+).+?'
        r'Platform: (?P<platform>\S+ \S+), .+?'
        r', Version (?P<ios>\S+),')

    result = {}
    match = re.search(regex, output, re.DOTALL)
    if match:
        device = match.group(1)
        result[device] = match.groupdict()
    return result


async def main():
    cdp_filename = 'sh_cdp_neighbors_detail_sw1.txt'
    async for neighbor in get_one_neighbor(cdp_filename):
        pprint(parse_neighbor(neighbor))


if __name__ == "__main__":
    asyncio.run(main())
