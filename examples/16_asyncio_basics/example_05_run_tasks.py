import asyncio
import time
from datetime import datetime
import random


async def delay_message(message):
    delay = random.choice(range(1, 11))
    print(f">>> start delay_message {message} sleep for {delay} sec")
    await asyncio.sleep(delay)
    print(f"<<< end   delay_message {message}")
    return message


async def main():
    start_time = datetime.now()
    print(f"Start main")
    tasks = [asyncio.create_task(delay_message(f"message {i}")) for i in range(1, 11)]
    result = [await task for task in tasks]
    print(f"Total {datetime.now() - start_time}")
    print(f"{result=}")


asyncio.run(main())
