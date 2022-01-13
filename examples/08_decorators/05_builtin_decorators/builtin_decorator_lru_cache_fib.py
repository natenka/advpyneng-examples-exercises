from functools import lru_cache


@lru_cache(maxsize=100)
def fib(n):
    print(f"{n=}")
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print([fib(n) for n in range(10)])
print([fib(n) for n in range(16)])
