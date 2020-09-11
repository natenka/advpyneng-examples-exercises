from functools import wraps


def all_args_str(func):
    print(f"Декорируем функцию {func}")

    @wraps(func)
    def wrapper(*args):
        if not all([isinstance(arg, str) for arg in args]):
            raise ValueError("Все аргументы должны быть строками")
        return func(*args)

    return wrapper


@all_args_str
def my_join(*args):
    return "|".join(args)


@all_args_str
def upper(string):
    "Конвертируем строку в upper"
    return string.upper()


@all_args_str
def lower(string):
    return string.lower()


@all_args_str
def capitalize(string):
    return string.capitalize()
