import re


def read_file(filename):
    with open(filename) as f:
        for index, line in enumerate(f, 1):
            line = line.rstrip()
            #print("READ", index, line)
            yield index, line


def filter_lines(iterable, regex):
    for index, line in iterable:
        if re.search(regex, line):
            #print("FILTER", index, line)
            yield line


def convert_to_lower(iterable):
    for line in iterable:
        #print("LOWER", line)
        yield line.lower()


if __name__ == "__main__":
    file_i = read_file("config_r1.txt")
    filt_i = filter_lines(file_i, "^interface")
    lower = map(str.lower, filt_i)
    for line in lower:
        print(line)
