import subprocess
import click


@click.command()
@click.argument("ip_address")
@click.option("--count", "-c", default=2, type=int, help="Number of packets")
def ping_ip(ip_address, count):
    """
    Ping IP address and return True/False
    """
    reply = subprocess.run(
        f"ping -c {count} -n {ip_address}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    if reply.returncode == 0:
        print(f"IP address {ip_address} is reachable")
    else:
        print(f"IP address {ip_address} is unreachable")


if __name__ == "__main__":
    ping_ip()
