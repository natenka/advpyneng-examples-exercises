from functools import update_wrapper

class verbose:
    def __init__(self, message):
        print("вызов verbose")
        self.msg = message

    def __call__(self, func):
        print(f"Декорация функции {func.__name__}")
        def inner(*args, **kwargs):
            print(f"У функции {func.__name__} такие аргументы")
            print(f"{args=}")
            print(f"{kwargs=}")
            result = func(*args, **kwargs)

        update_wrapper(wrapper=inner, wrapped=func)
        return inner



@verbose("hello")
def upper(string):
    return string.upper()

upper("a")
print(upper)
