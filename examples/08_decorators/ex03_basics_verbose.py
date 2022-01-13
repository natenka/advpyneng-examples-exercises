from functools import wraps


def verbose(func):
    print("вызываю декоратор verbose")

    @wraps(func)
    def inner(*args, **kwargs):
        print(f"У функции {func.__name__} такие аргументы")
        print(f"{args=}")
        print(f"{kwargs=}")
        result = func(*args, **kwargs)
        print(f"{result=}")
        return result

    return inner


@verbose  # upper = verbose(upper)
def upper(string):
    """return string.upper()"""
    return string.upper()


@verbose
def lower(string):
    return string.lower()


@verbose
def capitalize(string):
    return string.capitalize()
