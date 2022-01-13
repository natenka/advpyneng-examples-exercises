import asyncio


async def connect(ip, semaphore):
    print("Жду токена от семафора")
    await semaphore.acquire()
    print(f"Подключаюсь к {ip}")
    await asyncio.sleep(1)
    print(f"Ответ от {ip}")
    semaphore.release()


async def connect(ip, semaphore):
    print("Жду токена от семафора")
    async with semaphore:
        print(f"Подключаюсь к {ip}")
        await asyncio.sleep(1)
        print(f"Ответ от {ip}")


async def main():
    sem = asyncio.Semaphore(20)
    coroutines = [connect(i, sem) for i in range(100)]
    await asyncio.gather(*coroutines)


asyncio.run(main())
