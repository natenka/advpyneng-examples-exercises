

def mark1(func):
    func.mark = True
    return func


def add_mark(**kwargs):
    print("MARK", kwargs)
    def decorator(func):
        for attr, value in kwargs.items():
            setattr(func, attr, value)
        return func
    return decorator


mark = add_mark(mark=True)
test = add_mark(test=True)

@mark
def upper(string):
    """
    Возвращаем string в верхнем регистре
    """
    return string.upper()

