from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import repeat
import subprocess
from pprint import pprint
import click


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


@click.command()
@click.argument("ip-list", nargs=-1, required=True)
@click.option("-c", "--count", default=2, show_default=True)
@click.option(
    "-t",
    "--threads",
    default=2,
    show_default=True,
    type=click.IntRange(1, 10),
    help="указать кол-во потоков x",
)
def cli(ip_list, count, threads):
    print(f"{ip_list=}")
    ok, not_ok = ping_ip_addresses(ip_list, count, limit=threads)
    for ip in ok:
        click.secho(f"IP адрес {ip:20} пингуется", fg="green")
    for ip in not_ok:
        click.secho(f"IP адрес {ip:20} не пингуется", fg="red")


if __name__ == "__main__":
    cli()
