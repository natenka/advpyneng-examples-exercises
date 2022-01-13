import re
from pprint import pprint
from typing import List, Tuple
import yaml
from ex01_netmiko_optional import send_show


def parse_sh_cdp_neighbors(command_output: str) -> List[Tuple[str, ...]]:
    regex = re.compile(
        r"(?P<r_dev>\S+) +(?P<l_intf>\S+ \S+)"
        r" +\d+ +[\w ]+ +\S+ +(?P<r_intf>\S+ \S+)"
    )
    connect_list = []
    match_l_dev = re.search(r"(\S+)[>#]", command_output)
    if match_l_dev:
        l_dev = match_l_dev.group(1)
    for match in regex.finditer(command_output):
        neighbor = (l_dev, *match.group("l_intf", "r_dev", "r_intf"))
        connect_list.append(neighbor)
    return connect_list


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    output = send_show(devices[0], "sh cdp n")
    if output:
        print(output)
        pprint(parse_sh_cdp_neighbors(output), width=120)
