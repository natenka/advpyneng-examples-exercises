import re
from pprint import pprint
from typing import Iterator
from itertools import takewhile, dropwhile
import time


def read_by_neighbor(filename):
    with open(filename) as f:
        while True:
            start = dropwhile(lambda line: "Device ID" not in line, f)
            n_lines = takewhile(lambda line: "------" not in line, start)
            neighbor = "".join(n_lines)
            if not neighbor:
                return
            yield neighbor


def parse_cdp(neighbor):
    regex = (
        r"Device ID: (\S+).+?"
        r" +IP address: (?P<ip>\S+).+?"
        r"Cisco IOS Software, .+?, Version (?P<ios>\S+),"
    )
    match = re.search(regex, neighbor, re.DOTALL)
    if match:
        device = match.group(1)
        result = {device: match.groupdict()}
        return result


if __name__ == "__main__":
    data = read_by_neighbor("sh_cdp_neighbors_detail.txt")
    for n in data:
        # print(f"{n=}")
        print("#"*30)
        time.sleep(1)
        pprint(parse_cdp(n), width=120)
