# source https://twitter.com/nwkautomaniac/status/1447265484131422216?t=tLdBY52H681mCb01XUSJ5Q&s=03

from itertools import groupby


def vlan_range_str(vlans):
    range_str = []
    for _, num_gen in groupby(enumerate(vlans), key=lambda x: x[0] - x[1]):
        num_list = [item[1] for item in num_gen]
        first, last = num_list[0], num_list[-1]
        range_str.append(str(first) if first == last else f"{first}-{last}")
    return ",".join(range_str)


if __name__ == "__main__":
    vlans = [1, 2, 3, 4, 10, 11, 12, 100]
    print(vlan_range_str(sorted(vlans)))
