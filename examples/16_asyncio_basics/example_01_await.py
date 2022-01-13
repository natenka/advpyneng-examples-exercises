import asyncio
import time
from datetime import datetime


async def delay_message(delay, message):
    print(f">>> start delay_message {message}")
    await asyncio.sleep(delay)
    print(f"<<< end   delay_message {message}")


async def main():
    start_time = datetime.now()
    print(f"Start main")
    await delay_message(4, "message1")
    await delay_message(2, "message2")

    print(f"Total {datetime.now() - start_time}")


asyncio.run(main())
