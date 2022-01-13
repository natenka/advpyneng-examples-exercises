from functools import wraps

def all_args_str(func):
    print("декоратор all_args str")
    @wraps(func)
    def wrapper(*args):
        print("Проверяю аргументы")
        if not all(isinstance(arg, str) for arg in args):
            raise ValueError("Все аргументы должны быть строками")
        return func(*args)
    return wrapper


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


@all_args_str
@verbose
def upper(string):
    """return string.upper()"""
    return string.upper()


