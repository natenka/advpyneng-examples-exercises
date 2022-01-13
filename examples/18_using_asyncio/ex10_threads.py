import time
import logging
import random
from concurrent.futures import ThreadPoolExecutor


def scrapli_connect(device):
    time.sleep(1 + random.random())
    time.sleep(1 + random.random())
    return device


def main():
    devices = range(1000)
    with ThreadPoolExecutor(max_workers=300) as ex:
        results_map = ex.map(scrapli_connect, devices)
        results = [r for r in results_map]
    return results


if __name__ == "__main__":
    print(main())
