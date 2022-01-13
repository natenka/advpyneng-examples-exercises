def verbose_1(func):
    print(">>> START декорация verbose_1")
    def inner(*args, **kwargs):
        print(f">>>>>> verbose_1 Вызов функции {func.__name__}")
        result = func(*args, **kwargs)
        print(f"<<<<<< verbose_1 Получен результат функции {func.__name__}")
        return result

    print("<<< STOP декорация verbose_1")
    return inner


def verbose_2(func):
    print(">>> START декорация verbose_2")
    def inner(*args, **kwargs):
        print(f">>>>>> verbose_2 Вызов функции {func.__name__}")
        result = func(*args, **kwargs)
        print(f"<<<<<< verbose_2 Получен результат функции {func.__name__}")
        return result

    print("<<< STOP декорация verbose_2")
    return inner


@verbose_1
@verbose_2
def add(x, y):
    return x + y


print("#"*10)
print(add(10, 20))


"""
Вывод
>>> START декорация verbose_2
<<< STOP декорация verbose_2
>>> START декорация verbose_1
<<< STOP декорация verbose_1
##########
>>>>>> verbose_1 Вызов функции inner
>>>>>> verbose_2 Вызов функции add
<<<<<< verbose_2 Получен результат функции add
<<<<<< verbose_1 Получен результат функции inner
30
"""
