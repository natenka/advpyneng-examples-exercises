import asyncio
from datetime import datetime


async def delay_print(delay, message):
    await asyncio.sleep(delay)
    print(message)
    return message


async def main():
    print(f"start {datetime.now()}")
    task1 = asyncio.create_task(delay_print(4, "message 1"))
    task2 = asyncio.create_task(delay_print(2, "message 2"))
    print("Running...")
    task1_result = await task1
    print("Result:", task1_result)
    task2_result = await task2
    print("Result:", task2_result)
    print(f"end   {datetime.now()}")


if __name__ == "__main__":
    asyncio.run(main())

"""
$python example_03_create_task_extended.py
start 2019-11-02 08:58:28.478606
Running...
message 2
message 1
Result: message 1
Result: message 2
end   2019-11-02 08:58:32.481623
"""
