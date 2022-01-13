from functools import wraps


def d_1(func):
    print("Start decorator 1")

    def inner1(*args, **kwargs):
        print(f"Start inner1 {func.__name__=}")
        print("-" * 40)
        result1 = func(*args, **kwargs)
        print(f"{result1=}")
        print("-" * 40)
        return result1 * 100

    return inner1


def d_2(func):
    print("Start decorator 2")

    def inner2(*args, **kwargs):
        print(f"Start inner2 {func.__name__=}")
        print(">" * 40)
        result2 = func(*args, **kwargs)
        print(f"{result2=}")
        print("<" * 40)
        return result2 * 1000

    return inner2


def f():
    pass


# f = d_1(d_2(f))
