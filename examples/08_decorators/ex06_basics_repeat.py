version = 1


def mark(func):
    func.mark = True
    return func


def mark_new(func):
    func.mark_new = True
    return func


def f():
    pass

if version >= 1:
    f = mark(f)





from functools import wraps

def verbose(func):
    print("Декоратор verbose")
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"Вызываю функцию {func.__name__}")
        print(f"Аргументы {args=} {kwargs=}")
        result = func(*args, **kwargs)
        return result
    return inner


def kwargs_only(func):
    print("Декоратор verbose")
    @wraps(func)
    def inner(**kwargs):
        print(f"Вызываю функцию {func.__name__}")
        print(f"Аргументы {kwargs=}")
        result = func(**kwargs)
        return result
    return inner


def stringify(func):
    print("Декоратор return str")
    @wraps(func)
    def inner(*args, return_only_str=False, **kwargs):
        print(f"Вызываю функцию {func.__name__}")
        result = func(*args, **kwargs)
        if return_only_str:
            return str(result)
        else:
            return result
    return inner


