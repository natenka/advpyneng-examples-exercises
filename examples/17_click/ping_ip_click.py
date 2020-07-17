import subprocess
import click


def ping_ip(ip_address, count):
    """
    Ping IP address and return True/False
    """
    reply = subprocess.run(
        f"ping -c {count} -n {ip_address}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if reply.returncode == 0:
        return True
    else:
        return False


@click.command()
@click.argument("ip_address")
@click.option("--count", "-c", default=3, show_default=True)
def main(ip_address, count):
    if ping_ip(ip_address, count):
        print(f"IP-адрес {ip_address:15} пингуется")
    else:
        print(f"IP-адрес {ip_address:15} не пингуется")


if __name__ == "__main__":
    main()
