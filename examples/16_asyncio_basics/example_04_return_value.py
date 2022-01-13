import asyncio
import time
from datetime import datetime


async def delay_message(delay, message):
    print(f">>> start delay_message {message}")
    await asyncio.sleep(delay)
    print(f"<<< end   delay_message {message}")
    return message


async def main():
    start_time = datetime.now()
    print(f"Start main")
    task1 = asyncio.create_task(delay_message(4, "message1"))
    task2 = asyncio.create_task(delay_message(2, "message2"))

    result1 = await task1
    result2 = await task2
    print(f"Total {datetime.now() - start_time}")
    print(f"{result1=}, {result2=}")


asyncio.run(main())
