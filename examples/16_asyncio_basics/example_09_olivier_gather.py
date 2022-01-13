import asyncio
from datetime import datetime
import random


async def cook_potatoes(cooking_time):
    print(f">>> start potatoes")
    await asyncio.sleep(cooking_time)
    print(f"<<< end   potatoes""")
    return "potatoes done"


async def cook_carrots(cooking_time):
    print(f">>> start carrots")
    await asyncio.sleep(cooking_time)
    print(f"<<< end   carrots")
    return "carrots done"


async def cook_eggs(cooking_time):
    print(f">>> start eggs")
    await asyncio.sleep(cooking_time)
    print(f"<<< end   eggs")
    return "eggs done"


async def cutting(total_time):
    print(f">>> start cutting")
    await asyncio.sleep(total_time)
    print(f"<<< end   cutting")
    return "Salad done"



async def main():
    start_time = datetime.now()
    print(f"Start main")
    coroutines = [cook_potatoes(15), cook_carrots(15), cook_eggs(5)]
    results = await asyncio.gather(*coroutines)
    result = await cutting(10)
    print(f"Total {datetime.now() - start_time}")
    print(f"{result=}")


asyncio.run(main())

