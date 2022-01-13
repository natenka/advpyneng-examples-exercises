from functools import wraps


def verbose(format_str):
    print("Получаю аргументы декоратора и возвращаю декоратор")

    def decorator(func):
        print("Декорируем функцию")

        @wraps(func)
        def inner(*args, **kwargs):
            print(format_str.format(func.__name__))
            return func(*args, **kwargs)

        return inner

    return decorator


func_info_verbose = verbose("Вызываю функцию {}")
func_verbose = verbose("Вызываю функцию {}")


@func_info_verbose
def upper(string):
    return string.upper()


@func_info_verbose
def lower(string):
    return string.lower()


@func_info_verbose
def capitalize(string):
    return string.capitalize()
