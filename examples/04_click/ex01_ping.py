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


@click.command()
@click.argument("ip_address")
@click.option("-c", "--count", default=2, show_default=True, type=int)
def cli_interface(ip_address, count):
    print(f"{ip_address=}")
    print(f"{count=}")
    print(ping_ip(ip_address, count))


if __name__ == "__main__":
    cli_interface()
