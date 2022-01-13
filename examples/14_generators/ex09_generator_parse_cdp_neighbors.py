import re
from pprint import pprint
from typing import Iterator


def read_by_neighbor(filename: str) -> Iterator[str]:
    with open(filename) as f:
        neighbor = None
        for line in f:
            if "Device ID" in line:
                neighbor = line
            elif neighbor:
                if "--------" in line:
                    yield neighbor
                    neighbor = None
                else:
                    neighbor += line
        yield neighbor


def read_by_neighbor_2(filename: str) -> Iterator[str]:
    with open(filename) as f:
        all_n = f.read()

    match_all = re.finditer(r"Device ID.+?(-------------|$)", all_n, re.DOTALL)
    for m in match_all:
        yield m.group()


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
        pprint(parse_cdp(n), width=120)
        # pprint(n, width=120)
