# https://github.com/stellarbit/aioping
from pprint import pprint
import asyncio
import aioping


async def ping_ip(ip):
    try:
        delay = await aioping.ping(ip)
        delay = round(delay, 4)
        # print("Ping response in %s ms" % delay)
        return delay
    except TimeoutError:
        print("Timed out")


async def ping_ip_list(ip_list):
    coroutines = [ping_ip(ip) for ip in ip_list]
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3", "192.168.100.11"]
    results = asyncio.run(ping_ip_list(ip_list))
    print(results)
