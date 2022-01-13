import asyncio
from datetime import datetime


async def print_num(name):
    print(f"Start {name}")
    for _ in range(10):
        print(42)
        await asyncio.sleep(1)
        print(f"{name} working...")
        await asyncio.sleep(1)
    print(f"End {name}")


async def print_text(name):
    print(f"Start {name}")
    for _ in range(10):
        print("test")
        await asyncio.sleep(1.5)
    print(f"End {name}")


async def main():
    start  = datetime.now()
    print(f"Start {datetime.now()}")
    task1 = asyncio.create_task(print_num("task1"))
    task2 = asyncio.create_task(print_text("task2"))
    print(f"Running... {datetime.now() - start}")
    await task1
    await task2
    print(f"End {datetime.now() - start}")



