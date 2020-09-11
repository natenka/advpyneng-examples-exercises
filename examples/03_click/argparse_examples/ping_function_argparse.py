import subprocess
import argparse


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


def main():
    parser = argparse.ArgumentParser(description="Ping script")

    parser.add_argument("host", action="store", help="IP or name to ping")
    parser.add_argument(
        "-c",
        action="store",
        dest="count",
        default=2,
        type=int,
        help="Number of packets",
    )
    args = parser.parse_args()
    print(args)

    ping_ip(args.host, args.count)


if __name__ == "__main__":
    main()
