
def operations(num1, num2):
    def inner():
        pass

    def add():
        return num1 + num2

    def sub():
        return num1 - num2

    def mul():
        return num1 * num2

    inner.add_num = add
    inner.sub_num = sub
    inner.mul_num = mul

    return inner
