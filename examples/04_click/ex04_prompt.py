from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from netmiko import ConnectHandler
import yaml
import click

def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_devices(devices, command, limit=10):
    results = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [
            executor.submit(send_show_command, device, command)
            for device in devices
        ]
        for future in as_completed(futures):
            results.append(future.result())
    return results


@click.command()
@click.argument("command")
@click.argument("ip-list", nargs=-1, required=True)
@click.option("-u", "--username", prompt=True)
@click.option("-p", "--password", prompt=True, hide_input=True)
@click.option("-s", "--secret", prompt=True, hide_input=True)
def cli(command, ip_list, username, password, secret):
    print(command, ip_list, username, password, secret)
    device_params = {
        "device_type": "cisco_ios",
        "username": username,
        "password": password,
        "secret": secret,
    }

    device_list = [{**device_params, "host": ip} for ip in ip_list]

    result = send_command_to_devices(device_list, command)
    for ip, output in zip(ip_list, result):
        print(ip.center(30, "="))
        print(output)

if __name__ == "__main__":
    cli(auto_envvar_prefix="NETMIKO")

