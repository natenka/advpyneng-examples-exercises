def operations(num1, num2):
    operations.add_num = num1
    operations.sub_num = num2

    return operations

"""
In [2]: operations(2, 5)
Out[2]: <function __main__.operations(num1, num2)>

In [3]: operations.add_num
Out[3]: 2

In [4]: operations(20, 5)
Out[4]: <function __main__.operations(num1, num2)>

In [5]: operations.add_num
Out[5]: 20
"""

def operations(num1, num2):
    def add():
        return num1 + num2

    def sub():
        return num1 - num2

    operations.add_num = add
    operations.sub_num = sub

    return operations


def operations(num1, num2):
    def add():
        return num1 + num2

    def sub():
        return num1 - num2

    def dummy():
        pass

    dummy.add_num = add
    dummy.sub_num = sub

    return dummy



def multiply(num1):
    def inner(num2):
        return num1 * num2
    return inner

"""
In [27]: by_10 = multiply(num1=10)

In [28]: by_10(num2=2)
Out[28]: 20

In [29]: by_10(num2=3)
Out[29]: 30

In [30]: by_10(num2=10)
Out[30]: 100

In [31]: by_2 = multiply(num1=2)

In [32]: by_2(num2=100)
Out[32]: 200

In [33]: by_10(num2=10)
Out[33]: 100

In [34]: by_10(num2=3)
Out[34]: 30
"""
