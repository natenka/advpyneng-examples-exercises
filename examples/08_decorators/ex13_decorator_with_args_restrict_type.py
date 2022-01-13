from functools import wraps


def all_str(func):
    @wraps(func)
    def wrapper(*args):
        if not all(isinstance(arg, str) for arg in args):
            raise ValueError("Все аргументы должны быть строками")
        return func(*args)

    return wrapper


def arg_type(required_type):
    print(f"Создаем декоратор с типом {required_type}")

    def decorator(func):
        print("Вызываю декоратор")
        @wraps(func)
        def inner(*args):
            if not all(
                isinstance(arg, required_type) for arg in args
            ):
                raise ValueError(
                    f"Все аргументы должны быть {required_type.__name__}"
                )
            return func(*args)
        return inner
    return decorator

all_str = arg_type(str)
all_int = arg_type(int)

# f = all_str(f)



def arg_type2(required_type, func):
    print(f"Создаем декоратор с типом {required_type}")
    print("Вызываю декоратор")
    @wraps(func)
    def inner(*args):
        if not all(
            isinstance(arg, required_type) for arg in args
        ):
            raise ValueError(
                f"Все аргументы должны быть {required_type.__name__}"
            )
        return func(*args)
    return inner

def join(*args):
    return ",".join(args)

def f():
    pass

join = arg_type2(str, join)

