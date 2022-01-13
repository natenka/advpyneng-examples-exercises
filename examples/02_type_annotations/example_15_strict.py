def func1(a: str, b: str) -> str:
    return a + b


def func2(c, d):
    result = func1(4, 6)
    return c + d


if __name__ == "__main__":
    print(func2(4, 2))
