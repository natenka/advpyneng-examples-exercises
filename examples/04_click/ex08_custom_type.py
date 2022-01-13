from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import repeat
import subprocess
from pprint import pprint
import click
import ipaddress


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


def ping_ip_addresses(ip_addresses, count, limit):
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


class IsIPv4(click.ParamType):
    def convert(self, value, param, ctx):
        print("IsIPv4", value)
        try:
            ip = ipaddress.ip_address(value)
            return int(ip)
        except ValueError:
            self.fail(f"Все пропало: {value} не ip адрес")



@click.command()
@click.argument("ip-list", nargs=-1, required=True, type=IsIPv4())
@click.option("-c", "--count", default=2, show_default=True)
def cli(ip_list, count):
    print(f"{ip_list=}")


if __name__ == "__main__":
    cli()
