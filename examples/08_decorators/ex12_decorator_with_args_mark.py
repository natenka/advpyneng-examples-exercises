def basic_mark(func):
    print("Декорируем функцию с mark")
    func.mark = True
    return func


def add_mark(**kwargs):
    print("вызвали add_mark")

    def mark(func):
        print("Декорируем функцию с mark")
        for attr_name, value in kwargs.items():
            # func.mark = True
            setattr(func, attr_name, value)
        return func
    return mark

@add_mark(test=True)
def f():
    pass

# decorator = add_mark(test=True)
# f = decorator(f)
# print(f"{type(decorator)=}")
# print(f"{type(f)=}")
#
# f = add_mark(test=True)(f)



# test_and_verbose = add_mark(test=True, verbose=True)
# test = add_mark(test=True)
#
# @test_and_verbose
# def f1():
#     pass
#
#
# @test
# def f2():
#     pass

# decorator = add_mark(test=True, verbose=False)
# f1 = decorator(f1)


# @mark
# f = mark(f)
