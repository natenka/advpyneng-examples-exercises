import csv
from pprint import pprint
from collections import namedtuple

# "status","network","netmask","nexthop","metric","locprf","weight","path","origin"
# "*","1.0.0.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 15169","i"
# "*>","1.0.0.0","24","200.219.145.23",NA,NA,0,"53242 7738 15169","i"
# "*","1.0.4.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
# "*>","1.0.4.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 7545 56203","i"
Route = namedtuple(
    "Route",
    [
        "status",
        "network",
        "netmask",
        "nexthop",
        "metric",
        "locprf",
        "weight",
        "path",
        "origin",
    ],
)


def create_route(iterable):
    for index, route in iterable:
        yield index, Route(*route)


def read_file(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        for index, l_list in enumerate(reader, 1):
            # print("READ", index, l_list)
            yield index, l_list


def filter_by_nhop(iterable, nhop):
    for index, route in iterable:
        if route.nexthop == nhop:
            yield index, route


def filter_by_mask(iterable, mask):
    for index, route in iterable:
        if route.netmask == mask:
            yield index, route


if __name__ == "__main__":
    file = read_file("rib.csv")
    n_tuples = create_route(file)
    f_23 = filter_by_nhop(n_tuples, "200.219.145.23")
    mask_22 = filter_by_mask(f_23, "22")
    data = [next(mask_22) for _ in range(10)]
    pprint(data)
    # print(next(mask_22))
    # print(next(mask_22))
    # print(next(mask_22))
    # print(next(mask_22))
    # print(next(mask_22))
    # print(next(mask_22))
