import asyncio


async def connect(ip, semaphore):
    async with semaphore:
        print(f"Подключаюсь к {ip}")
        await asyncio.sleep(1)
        print(f"Ответ от {ip}")


async def main():
    sem = asyncio.Semaphore(20)
    coroutines = [connect(i, sem) for i in range(500)]
    await asyncio.gather(*coroutines)


asyncio.run(main())
