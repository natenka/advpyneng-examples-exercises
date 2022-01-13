import asyncio
from datetime import datetime


async def delay_for(sec, name):
    print(f"START {name}")
    await asyncio.sleep(sec)
    print(f"STOP  {name}")
    return name


async def main():
    print(f">>> START {datetime.now()}")
    task1 = asyncio.create_task(delay_for(5, "task1"))
    task2 = asyncio.create_task(delay_for(2, "task2"))
    print(">>> ALL TASKS RUNNING")
    result2 = await task2
    result1 = await task1
    print(f">>> STOP  {datetime.now()}")
    print(f"{result1=}")
    print(f"{result2=}")


async def main_prev():
    print(f">>> START {datetime.now()}")
    result1 = await delay_for(5, "task1")
    result2 = await delay_for(2, "task2")
    print(">>> ALL TASKS RUNNING")
    print(f">>> STOP  {datetime.now()}")


if __name__ == "__main__":
    asyncio.run(main())
