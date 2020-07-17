import subprocess


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


if __name__ == "__main__":
    ip = "8.8.8.8"
    if ping_ip(ip, count=3):
        print(f"IP-адрес {ip:15} пингуется")
    else:
        print(f"IP-адрес {ip:15} не пингуется")

