import asyncio
from functools import wraps


def restrict_args_type(required_type):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args):
            if not all(isinstance(arg, required_type) for arg in args):
                raise ValueError(f"Все аргументы должны быть {required_type.__name__}")
            return await func(*args)

        return wrapper

    return decorator


@restrict_args_type(str)
async def to_upper(*args):
    await asyncio.sleep(3)
    result = [s.upper() for s in args]
    return result


if __name__ == "__main__":
    asyncio.run(to_upper("a", "b"))
    asyncio.run(to_upper("a", 1))
