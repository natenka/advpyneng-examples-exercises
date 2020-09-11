import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url, ssl=False) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "http://python.org")
        print(html)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
