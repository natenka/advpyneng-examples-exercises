def multiply(num1):
    def inner(num2):
        return num1 * num2
    return inner


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

