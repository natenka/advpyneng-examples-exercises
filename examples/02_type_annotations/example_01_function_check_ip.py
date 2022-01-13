import ipaddress


def check_ip(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as err:
        return False


if __name__ == "__main__":
    print(check_ip("10.1.1.1"))
    print(check_ip(500))
