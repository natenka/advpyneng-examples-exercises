from functools import wraps
from inspect import signature, Signature, Parameter


def add_debug_param(func):
    @wraps(func)
    def inner(*args, debug=False, **kwargs):
        if debug:
            print(f"Вызов функции {func.__name__} с аргументами {args}, {kwargs}")
        return func(*args, **kwargs)

    original_signature = signature(func)
    new_params = list(original_signature.parameters.values())
    debug_param = Parameter("debug", kind=Parameter.POSITIONAL_OR_KEYWORD, default=False)
    new_params.append(debug_param)
    new_sig = Signature(parameters=new_params)
    inner.__signature__ = new_sig
    return inner


@add_debug_param
def upper(string):
    return string.upper()


@add_debug_param
def summ(a, b):
    return a + b





