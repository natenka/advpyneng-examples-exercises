import asyncio
from datetime import datetime


async def delay_message(delay, message):
    print(">>> start delay_message")
    await asyncio.sleep(delay)
    print("<<<", message)


async def main():
    print(f"Start {datetime.now()}")
    await delay_message(4, "Hello")
    await delay_message(2, "world")
    print(f"End   {datetime.now()}")


if __name__ == "__main__":
    asyncio.run(main())

# $ python await_example.py
# Start 2019-10-31 11:56:30.995001
# >>> start delay_message
# <<< Hello
# >>> start delay_message
# <<< world
# End   2019-10-31 11:56:37.000033
