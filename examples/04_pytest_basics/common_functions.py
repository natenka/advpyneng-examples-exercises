import inspect


def check_attr_or_method(obj, attr=None, method=None):
    if attr:
        assert getattr(obj, attr, None) != None, "Атрибут не найден"
        assert not inspect.ismethod(
            getattr(obj, attr)
        ), f"{attr} должен быть переменной, а не методом"
    if method:
        assert getattr(obj, method, None) != None, "Метод не найден"
        assert inspect.ismethod(
            getattr(obj, method)
        ), f"{method} должен быть методом, а не переменной"


def check_class_exists(module, class_name):
    assert hasattr(module, class_name) and inspect.isclass(
        getattr(module, class_name)
    ), f"Надо создать класс с именем {class_name}"


def check_function_exists(module, function_name):
    assert hasattr(module, function_name) and inspect.isfunction(
        getattr(module, function_name)
    ), f"Надо создать функцию с именем {function_name}"


def check_function_params(function, param_count, param_names=None):
    arg_info = inspect.getfullargspec(function)
    assert (
        len(arg_info.args) == param_count
    ), f"У функции {function.__name__} должно быть {param_count} параметров"
    if param_names:
        assert set(arg_info.args) == set(
            param_names
        ), f"У функции должны быть такие параметры: {','.join(param_names)}"


def get_func_params_default_value(function):
    func_sig = inspect.signature(function)
    return {
        k: v.default
        for k, v in func_sig.parameters.items()
        if v.default is not inspect.Parameter.empty
    }
