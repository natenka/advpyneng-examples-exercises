import subprocess
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


def ping_ip_addresses(ip_addresses, count):
    for ip in ip_addresses:
        if ping_ip(ip, count):
            yield ip, True
        else:
            yield ip, False


@click.command()
@click.argument("ip_addresses", nargs=-1, required=True)
@click.option("--count", "-c", default=2, type=int, help="Number of packets")
def main(ip_addresses, count):
    """
    Ping IP_ADDRESS
    """
    for ip, status in ping_ip_addresses(ip_addresses, count):
        if status:
            print(f"IP-адрес {ip:15} пингуется")
        else:
            print(f"IP-адрес {ip:15} не пингуется")


if __name__ == "__main__":
    main()

"""
$ python example_02_ping_ip_list_generator.py 8.8.8.8 8.8.4.4 10.1.1.1 192.168.100.1
IP-адрес 8.8.8.8         пингуется
IP-адрес 8.8.4.4         пингуется
IP-адрес 10.1.1.1        не пингуется
IP-адрес 192.168.100.1   пингуется
"""
