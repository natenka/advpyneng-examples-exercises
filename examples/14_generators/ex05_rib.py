import csv

# "status","network","netmask","nexthop","metric","locprf","weight","path","origin"
# "*","1.0.0.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 15169","i"
# "*>","1.0.0.0","24","200.219.145.23",NA,NA,0,"53242 7738 15169","i"
# "*","1.0.4.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
# "*>","1.0.4.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 7545 56203","i"

def read_file(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        for index, l_list in enumerate(reader, 1):
            #print("READ", index, l_list)
            yield index, l_list


def filter_by_nhop(iterable, nhop):
    for index, prefix in iterable:
        if prefix[3] == nhop:
            yield index, prefix


def filter_by_mask(iterable, mask):
    for index, prefix in iterable:
        if prefix[2] == mask:
            yield index, prefix


if __name__ == "__main__":
    file = read_file("rib.csv")
    f_23 = filter_by_nhop(file, "200.219.145.23")
    mask_22 = filter_by_mask(f_23, "22")
    print(next(mask_22))
    print(next(mask_22))
    print(next(mask_22))
    print(next(mask_22))
    print(next(mask_22))
    print(next(mask_22))
