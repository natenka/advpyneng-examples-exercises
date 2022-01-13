# -*- coding: utf-8 -*-
"""
Задание 8.2

Переделать декоратор all_args_str таким образом, чтобы он проверял
не только позиционные аргументы, но и ключевые тоже.

In [2]: concat_str(str1='b', str2='a')
Out[2]: 'ba'

In [3]: concat_str(str1='b', str2=1)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-3-08af972add0a> in <module>
----> 1 concat_str(str1='b', str2=1)
...
ValueError: Все аргументы должны быть строками


In [4]: concat_str('b', 1)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-4-864f6fda8c8b> in <module>
----> 1 concat_str('b', 1)
...
ValueError: Все аргументы должны быть строками

"""


def all_args_str(func):
    def wrapper(*args):
        if not all(isinstance(arg, str) for arg in args):
            raise ValueError("Все аргументы должны быть строками")
        return func(*args)

    return wrapper


@all_args_str
def concat_str(str1, str2):
    return str1 + str2


if __name__ == "__main__":
    # пример вызова с передачей ключевых аргументов
    # до выполнения задания, будет вызывать ошибку
    concat_str(str1=2, str2=1)
