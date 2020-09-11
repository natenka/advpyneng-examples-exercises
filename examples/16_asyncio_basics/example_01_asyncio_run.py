import asyncio
from datetime import datetime


async def delay_message(delay, message):
    print(">>> start delay_message")
    await asyncio.sleep(delay)
    print("<<<", message)


if __name__ == "__main__":
    asyncio.run(delay_message(4, "Работаю..."))

# $ python asyncio_run_example.py
# >>> start delay_message
# <<< Работаю...
