from netmiko import ConnectHandler

r1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}
r2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.2',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}

def connect_ssh(device):
    ssh = ConnectHandler(**device)
    ssh.enable()
    def send_command(command):
        return ssh.send_command(command)
    return send_command
