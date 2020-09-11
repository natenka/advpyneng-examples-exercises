import re
from pprint import pprint
from itertools import dropwhile, takewhile
from more_itertools import split_before


def get_one_neighbor(filename):
    with open(filename) as f:
        neighbors = split_before(f, lambda x: "Device ID" in x)
        next(neighbors)  # избавляемся от текста до соседей
        for lines in neighbors:
            neighbor = "".join(lines)
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
