# source https://stackabuse.com/overview-of-async-io-in-python-3-7/
import sys
import asyncio
import aiohttp
import json
import datetime


async def get_json(client, url):
    async with client.get(url, ssl=False) as response:
        assert response.status == 200
        return await response.read()


async def get_reddit_top(subreddit, client, numposts):
    data = await get_json(
        client,
        "https://www.reddit.com/r/"
        + subreddit
        + "/top.json?sort=top&t=day&limit="
        + str(numposts),
    )

    print(f"\n/r/{subreddit}:")

    j = json.loads(data.decode("utf-8"))
    for i in j["data"]["children"]:
        score = i["data"]["score"]
        title = i["data"]["title"]
        link = i["data"]["url"]
        print("\t" + str(score) + ": " + title + "\n\t\t(" + link + ")")


async def main():
    print(datetime.datetime.now().strftime("%A, %B %d, %I:%M %p"))
    print("---------------------------")
    loop = asyncio.get_running_loop()
    async with aiohttp.ClientSession(loop=loop) as client:
        await asyncio.gather(
            get_reddit_top("python", client, 3),
            get_reddit_top("programming", client, 4),
            get_reddit_top("asyncio", client, 2),
            get_reddit_top("dailyprogrammer", client, 1),
        )


asyncio.run(main())
