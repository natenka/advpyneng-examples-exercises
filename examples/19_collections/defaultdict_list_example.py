from pprint import pprint
from collections import defaultdict


def get_ip_from_cfg(filename):
    result = defaultdict(list)
    with open(filename) as f:
        for line in f:
            if line.startswith("interface"):
                intf = line.split()[-1]
            elif line.startswith(" switchport"):
                result[intf].append(line.strip())
    return result


if __name__ == "__main__":
    pprint(get_ip_from_cfg("config_sw1.txt"))
