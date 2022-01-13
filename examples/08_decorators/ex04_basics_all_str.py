def all_args_str(func):
    def wrapper(*args):
        if not all(isinstance(arg, str) for arg in args):
            raise ValueError("Все аргументы должны быть строками")
        return func(*args)

    return wrapper

