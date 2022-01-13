import time
import asyncio
from datetime import datetime


def timed(func):
    async def wrapper(*args, **kwargs):
        start = datetime.now()
        result = await func(*args, **kwargs)
        print(f"Время выполнения {datetime.now() - start}")
        return result
    return wrapper


#f = timed(f)
@timed
async def f():
    await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(f()) # wrapped()
