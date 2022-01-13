import asyncio
from pprint import pprint
from functools import wraps
import inspect
import yaml
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
from devices_scrapli import devices as devices_ssh


def verbose(func):
    if inspect.iscoroutinefunction(func):
        @wraps(func)
        async def inner(*args, verbose=False, **kwargs):
            if verbose:
                print(f"{args=}")
                print(f"{kwargs=}")
            result = await func(*args, **kwargs)
            return result
        return inner
    else:
        @wraps(func)
        def inner(*args, verbose=False, **kwargs):
            if verbose:
                print(f"{args=}")
                print(f"{kwargs=}")
            result = func(*args, **kwargs)
            return result
        return inner

# send_show = verbose(send_show)

@verbose
async def send_show(device, command):
    print(f">>> connect to {device['host']}")
    try:
        async with AsyncScrapli(**device) as conn:
            result = await conn.send_command(command)
            print(f"<<< {device['host']}")
            return result.result
    except ScrapliException as error:
        print(error, device["host"])


if __name__ == "__main__":
    with open("devices_scrapli.yaml") as f:
        devices = yaml.safe_load(f)
        r1 = devices[0]
    result = asyncio.run(send_show(r1, "sh clock", verbose=True))
    pprint(result, width=120)
