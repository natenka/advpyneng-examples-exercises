
def tag(func):
    print(f"Декорируем функцию {func.__name__}")
    func.tag = True
    return func

@tag # upper = tag(upper)
def upper(string):
    print("вызов upper")
    return string.upper()

@tag
def lower(string):
    return string.lower()


def capitalize(string):
    return string.capitalize()

