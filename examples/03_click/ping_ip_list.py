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
        encoding="utf-8",
    )
    if reply.returncode == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    ip_list = ["8.8.8.8", "8.8.4.4", "10.1.1.1", "192.168.100.1"]
    for ip in ip_list:
        if ping_ip(ip, count=3):
            print(f"IP-адрес {ip:15} пингуется")
        else:
            print(f"IP-адрес {ip:15} не пингуется")
