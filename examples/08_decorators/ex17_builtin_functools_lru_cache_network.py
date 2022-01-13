from functools import lru_cache


@lru_cache
def send_show_command(host, device_type, username, password, show):
    with ConnectHandler(
        host=host, device_type=device_type, username=username, password=password
    ) as ssh:
        result = ssh.send_command(show)
    return result


r1 = {
    "device_type": "cisco_ios",
    "host": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
}
send_show_command(**r1, show="sh clock")
send_show_command(**r1, show="sh clock")
send_show_command(**r1, show="sh clock")
