from functools import wraps


def strict_args_type(required_type):
    def decorator(func):
        print(f"Декорируем функцию {func}")

        @wraps(func)
        def wrapper(*args):
            if not all([isinstance(arg, required_type) for arg in args]):
                raise ValueError(
                    f"Все аргументы должны быть типа {required_type.__name__}"
                )
            return func(*args)

        return wrapper

    return decorator


strict_str = strict_args_type(str)
strict_int = strict_args_type(int)


def my_join(*args):
    return "|".join(args)


def upper(string):
    "Конвертируем строку в upper"
    return string.upper()


def lower(string):
    return string.lower()


def capitalize(string):
    return string.capitalize()


if True:
    my_join = decorator(my_join)
else:
    my_join = decor2(my_join)

if True:
    decorator = strict_args_type
else:
    decorator = strict
