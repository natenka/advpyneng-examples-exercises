import time


def upper(string):
    return string.upper()


def delay(sec, func, *args, **kwargs):
    print(f"delay {sec=} {func=}")
    print(args)
    print(kwargs)
    time.sleep(sec)
    result = func(*args, **kwargs)
    return result


def apply_chain(functions, arg):
    for f in functions:
        arg = f(arg)
    return arg


def parse_file(filename):
    def parse(open_file):
        for line in open_file:
            print(line)

    if type(filename) == str:
        with open(filename) as f:
            parse(f)
    else:
        parse(filename)

