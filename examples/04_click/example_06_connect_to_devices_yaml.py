import click
from netmiko import ConnectHandler
import yaml
from pprint import pprint


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_cisco_devices(device_list, command):
    result = {}
    with click.progressbar(device_list) as bar:
        for device in bar:
            ip = device["host"]
            result[ip] = send_show_command(device, command)
    return result

@click.command()
@click.argument("command")
@click.option("--device-params", type=click.File("r"), required=True)
@click.option("--output-file", type=click.File("w"), required=True)
def cli(command, device_params, output_file):
    print("CLICK PARAMS:", command, device_params)
    devices = yaml.safe_load(device_params)
    result = send_command_to_cisco_devices(devices, command)
    yaml.dump(result, output_file)

if __name__ == "__main__":
    cli()
