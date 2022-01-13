from pprint import pprint
import re


def get_interfaces_from_cfg(config_str):
    match_all = re.finditer(r"^interface (\S+)", config_str, re.MULTILINE)
    interfaces = [m.group(1) for m in match_all]
    return interfaces


if __name__ == "__main__":
    with open("config_sw1.txt") as f:
        pprint(get_interfaces_from_cfg(f.read()))
    with open("config_sw2.txt") as f:
        pprint(get_interfaces_from_cfg(f.read()))
