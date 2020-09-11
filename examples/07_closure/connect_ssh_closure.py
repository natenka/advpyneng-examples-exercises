from netmiko import ConnectHandler

device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}


def netmiko_ssh(**params_dict):
    ssh = ConnectHandler(**params_dict)
    ssh.enable()

    def send_show_command(command):
        return ssh.send_command(command)

    netmiko_ssh.send_show_command = send_show_command
    return send_show_command
