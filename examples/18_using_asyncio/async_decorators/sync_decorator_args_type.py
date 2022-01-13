from functools import wraps
import asyncio


def restrict_args_type(required_type):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args):
            if not all(isinstance(arg, required_type) for arg in args):
                raise ValueError(
                    f'Все аргументы должны быть {required_type.__name__}'
                )
            return await func(*args)
        return wrapper
    return decorator


@restrict_args_type(str)
async def to_upper(*args):
    result = [s.upper() for s in args]
    await asyncio.sleep(1)
    return result


print(asyncio.run(to_upper("a")))
print(asyncio.run(to_upper(1)))
