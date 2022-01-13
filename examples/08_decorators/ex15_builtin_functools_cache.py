from functools import cache, lru_cache


@cache
def factorial(n):
    print(f"{n=}")
    return n * factorial(n-1) if n else 1


print(f"{factorial(4)=}")
print(f"{factorial(5)=}")
print(f"{factorial(6)=}")


def mycache(func):
    cache_dict = {}
    def inner(*args):
        if args in cache_dict:
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        # return result
        return cache_dict[args]
    return inner
