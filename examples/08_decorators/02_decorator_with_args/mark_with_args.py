def mark(**kwargs):
    print(f"Получил аргументы {kwargs}")

    def decorator(func):
        print(f"добавляем атрибуты функции {kwargs}")
        for name, value in kwargs.items():
            setattr(func, name, value)
        return func

    decorator.data = kwargs
    return decorator


def mark_2(**kwargs_mark):
    print(f"Получил аргументы {kwargs_mark}")

    def decorator(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        print(f"добавляем атрибуты функции {kwargs_mark}")
        for name, value in kwargs_mark.items():
            setattr(inner, name, value)
        return inner

    return decorator
