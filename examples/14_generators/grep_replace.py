import time
import re


def grep(iterable, regex):
    for idx, line in enumerate(iterable, 1):
        if re.search(regex, line):
            print("Строка", idx)
            yield line.rstrip()


def replace(iterable, old, new):
    for item in iterable:
        print("Замена строки")
        yield re.sub(old, new, item)


def grep_old(iterable, regex):
    result = []
    for idx, line in enumerate(iterable, 1):
        if re.search(regex, line):
            print("Строка", idx)
            result.append(line.rstrip())
    return result


def replace_old(iterable, old, new):
    result = []
    for item in iterable:
        print("Замена строки")
        result.append(re.sub(old, new, item))
    return result
