from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import repeat
import subprocess
from pprint import pprint


def ping_ip(ip_address, count):
    """
    Ping IP_ADDRESS and return True/False
    """
    reply = subprocess.run(
        f"ping -c {count} -n {ip_address}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    if reply.returncode == 0:
        return True
    else:
        return False


def ping_ip_addresses(ip_addresses, count, limit=10):
    reachable = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        results = executor.map(ping_ip, ip_addresses, repeat(count))
        for ip, status in zip(ip_addresses, results):
            if status:
                reachable.append(ip)
            else:
                unreachable.append(ip)
    return reachable, unreachable


if __name__ == "__main__":
    ip_list = ["8.8.8.8", "8.8.4.4", "10.1.1.1", "192.168.100.1"]
    pprint(ping_ip_addresses(ip_list, count=1))
