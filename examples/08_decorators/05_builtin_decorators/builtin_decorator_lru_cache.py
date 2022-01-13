from functools import lru_cache
from netmiko import ConnectHandler
import time


device_params = {
    "host": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    "device_type": "cisco_ios",
}


@lru_cache(maxsize=1)
def send_show_command(host, username, password, secret, device_type, show_command):
    with ConnectHandler(
        host=host,
        username=username,
        password=password,
        secret=secret,
        device_type=device_type,
    ) as ssh:
        ssh.enable()
        print(f"Вызываю команду {show_command}")
        result = ssh.send_command(show_command)
    return result

