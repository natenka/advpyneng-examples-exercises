from functools import cache, lru_cache


@lru_cache(maxsize=10)
def factorial(n):
    print(f"{n=}")
    return n * factorial(n-1) if n else 1


print(f"{factorial(4)=}")
print(f"{factorial(5)=}")
print(f"{factorial(6)=}")


def my_lru_cache(maxsize=128):
    def mycache(func):
        cache_dict = {}
        def inner(*args):
            if len(cache_dict) >= maxsize:
                first_key = list(cache_dict.keys())[0]
                cache_dict.pop(first_key)
            if args in cache_dict:
                return cache_dict[args]
            result = func(*args)
            cache_dict[args] = result
            return result
        return inner
    return mycache
