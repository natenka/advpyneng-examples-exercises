from datetime import datetime
from netmiko import ConnectHandler

device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}


def timecode(function):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = function(*args, **kwargs)
        print(">>> Функция выполнялась:", datetime.now() - start_time)
        return result

    return wrapper


# send_show_command = timecode(send_show_command)


@timecode
def send_show_command(params, command):
    with ConnectHandler(**params) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


if __name__ == "__main__":
    print(send_show_command(device_params, "sh clock"))
