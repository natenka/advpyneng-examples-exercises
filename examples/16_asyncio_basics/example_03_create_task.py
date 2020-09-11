import asyncio
from datetime import datetime


async def delay_message(delay, message):
    print(">>> start delay_message")
    await asyncio.sleep(delay)
    print("<<<", message)


async def main():
    print(f"Start {datetime.now()}")
    task1 = asyncio.create_task(delay_message(4, "Hello"))
    task2 = asyncio.create_task(delay_message(2, "world"))

    await task1
    await task2
    print(f"End   {datetime.now()}")


if __name__ == "__main__":
    asyncio.run(main())

# Start 2019-10-30 10:18:39.489131
# >>> start delay_message
# >>> start delay_message
# <<< world
# <<< Hello
# End   2019-10-30 10:18:43.494321
