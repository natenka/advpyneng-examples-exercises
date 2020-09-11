import re
from pprint import pprint


def get_one_neighbor(filename):
    with open(filename) as f:
        line = ""
        while True:
            while not "Device ID" in line:
                line = f.readline()
            neighbor = line
            for line in f:
                if "----------" in line:
                    break
                neighbor += line
            yield neighbor
            line = f.readline()
            if not line:
                return


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
    data = get_one_neighbor("sh_cdp_neighbors_detail_sw1.txt")
    for n in data:
        pprint(parse_neighbor(n), width=120)
