
def verbose(func):
    print("Вызываю декоратор verbose")

    def inner(*args, **kwargs):
        print(f"У функции {func.__name__} такие "
              f"аргументы {','.join(map(str, args))}")
        return func(*args, **kwargs)

    return inner

def kwargs_only(func):
    print("Вызываю декоратор kwargs_only")

    def inner(**kwargs):
        print(f"Функция {func.__name__}")
        print(kwargs)
        return func(**kwargs) # func(string="test")

    return inner


def mark(func):
    func.mark = True
    return func

regist_functions = []

def register(func):
    regist_functions.append(func)
    return func

from functools import wraps

def debug(func):
    print("Вызываю декоратор debug")
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"Вызываю функцию {func.__name__}")
        print(args, kwargs)
        result = func(*args, **kwargs)
        return result
    return inner


@debug
def upper(string):
    """
    Возвращаем string в верхнем регистре
    """
    return string.upper()


@debug
def summ(a, b):
    return a + b


