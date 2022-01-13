from functools import wraps

help_str = []

def d_1(func):
    print("Start decorator 1")

    def inner1(*args, **kwargs):
        print(f"Start inner 1 func={func.__name__}")
        help_str.append(f"Start inner 1 func={func.__name__}")
        result = func(*args, **kwargs)
        print("End inner 1")
        return result
    return inner1

def d_2(func):
    print("Start decorator 2")

    def inner2(*args, **kwargs):
        print(f"Start inner 2 func={func.__name__}")
        help_str.append(f"Start inner 2 func={func.__name__}")
        result = func(*args, **kwargs)
        print("End inner 2")
        return result
    return inner2


#@d_1
#@d_2
def add(a, b):
    print(f"Start add")
    return a + b


#add = d_1(d_2(add))
inner2 = d_2(func=add)
inner1 = d_1(func=inner2)
add = inner1
