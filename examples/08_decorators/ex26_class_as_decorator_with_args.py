from functools import update_wrapper

class Verbose:
    def __init__(self, message):
        self.message = message

    def __call__(self, func):
        print("Декорация")
        def inner(*args, **kwargs):
            print(self.message)
            print(f"У функции {func.__name__} такие аргументы")
            print(f"{args=}")
            print(f"{kwargs=}")
            result = func(*args, **kwargs)
            print(f"{result=}")
            return result
        update_wrapper(wrapper=inner, wrapped=func)
        return inner


def upper(string):
    return string.upper()

decorator = Verbose("Hello")
upper = decorator(upper)
print(f"{upper('a')=}")
print(upper)
