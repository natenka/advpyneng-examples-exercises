from functools import wraps


def arg_type(required_type, verbose=True):
    if verbose: print(f"Создаем декоратор с типом {required_type}")

    def decorator(func):
        if verbose: print("Вызываю декоратор")
        @wraps(func)
        def inner(*args):
            if verbose: print(f"Вызываю фукнцию {func.__name__}")
            if not all(
                isinstance(arg, required_type) for arg in args
            ):
                raise ValueError(
                    f"Все аргументы должны быть {required_type.__name__}"
                )
            return func(*args)
        return inner
    return decorator
