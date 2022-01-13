def countdown(n):
    print("вызываем countdown")
    def inner():
        print("вызываем inner")
        nonlocal n
        current = n
        n -= 1
        # n = n -1
        return current
    return inner
