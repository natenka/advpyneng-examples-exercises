import re
from pprint import pprint
from typing import Iterator
from itertools import takewhile, dropwhile
import time


def read_by_neighbor(filename: str) -> Iterator[str]:
    with open(filename) as f:
        line = ""
        while True:
            start = dropwhile(lambda x: "Device ID" not in x, f)
            neighbor = takewhile(lambda x: "----------" not in x, start)
            neighbor_str = "".join(neighbor)
            if not neighbor_str:
                return
            yield neighbor_str


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
        # print(n)
        print("#"*30)
        pprint(parse_cdp(n), width=120)
