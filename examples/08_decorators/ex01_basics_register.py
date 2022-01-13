
string_op = []

def register(func):
    print(f"Декорируем функцию {func.__name__}")
    string_op.append(func)
    return func

@register # upper = register(upper)
def upper(string):
    print("вызов upper")
    return string.upper()

@register
def lower(string):
    return string.lower()


@register
def capitalize(string):
    return string.capitalize()

print(string_op)
