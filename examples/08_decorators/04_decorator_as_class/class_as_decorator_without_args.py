
class verbose:
    def __init__(self, func):
        print(f"Декорация функции {func.__name__}")
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"У функции {self.func.__name__} такие аргументы")
        print(f"{args=}")
        print(f"{kwargs=}")
        result = self.func(*args, **kwargs)
        return result


@verbose
def upper(string):
    return string.upper()

upper("a")
# upper = verbose(upper)
print(upper)
