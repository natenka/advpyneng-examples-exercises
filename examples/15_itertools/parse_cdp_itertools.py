import re
from pprint import pprint
from itertools import dropwhile, takewhile


def get_one_neighbor(filename):
    with open(filename) as f:
        line = ""
        while True:
            result = dropwhile(lambda s: "Device ID" not in s, f)
            neighbor = takewhile(lambda s: "-----------" not in s, result)
            neighbor = "".join(neighbor)
            if not neighbor:
                return
            yield neighbor


def parse_neighbor(output):
    regex = (
        r"Device ID: (\S+).+?"
        r" IP address: (?P<ip>\S+).+?"
        r"Platform: (?P<platform>\S+ \S+), .+?"
        r", Version (?P<ios>\S+),"
    )

    result = {}
    match = re.search(regex, output, re.DOTALL)
    if match:
        device = match.group(1)
        result[device] = match.groupdict()
    return result


if __name__ == "__main__":
    data = get_one_neighbor("sh_cdp_neighbors_detail.txt")
    for n in data:
        pprint(parse_neighbor(n), width=120)
