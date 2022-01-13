import ipaddress


def check_ip(ip):
    if not isinstance(ip, str):
        return False
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

