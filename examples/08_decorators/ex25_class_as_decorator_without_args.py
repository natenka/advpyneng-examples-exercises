def verbose(func):
    print("Декорируем")
    def inner(*args, **kwargs):
        print(f"У функции {func.__name__} такие аргументы")
        print(f"{args=}")
        print(f"{kwargs=}")
        result = func(*args, **kwargs)
        print(f"{result=}")
        return result
    return inner


class Verbose:
    def __init__(self, func):
        print("Декорируем")
        self.func = func

    def __call__(self, *args, **kwargs):
        print("__call__")
        print(args, kwargs)
        return self.func(*args, **kwargs)


#upper = Verbose(upper)
#upper("a")
