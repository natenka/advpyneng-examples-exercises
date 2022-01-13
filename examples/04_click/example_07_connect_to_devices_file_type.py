import click
from netmiko import ConnectHandler
import yaml


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_cisco_devices(device_list, command):
    result = {}
    with click.progressbar(device_list, label="Connecting to devices") as bar:
        for device in bar:
            ip = device["host"]
            result[ip] = send_show_command(device, command)
    return result


@click.command()
@click.argument("command")
@click.option("--yaml-params", "-y", type=click.File("r"), required=True)
@click.option("--write-output-to-file", "-o", type=click.File("w"))
def main(command, yaml_params, write_output_to_file):
    devices = yaml.safe_load(yaml_params)

    result_dict = send_command_to_cisco_devices(devices, command)
    for ip, output in result_dict.items():
        if write_output_to_file:
            write_output_to_file.write(ip.center(30, "="))
            write_output_to_file.write(output)
        else:
            print(ip.center(30, "="))
            print(output)


if __name__ == "__main__":
    main()

"""
$ python example_07_connect_to_devices_file_type.py "sh ip int br" -y devices.yaml
Connecting to devices  [####################################]  100%
========192.168.100.1=========
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                19.1.1.1        YES NVRAM  up                    up
Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
Loopback0                  4.4.4.4         YES NVRAM  up                    up
Loopback55                 5.5.5.5         YES manual up                    up
Loopback90                 90.1.1.1        YES NVRAM  up                    up
========192.168.100.2=========
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down
Ethernet0/2                unassigned      YES NVRAM  administratively down down
Ethernet0/3                unassigned      YES NVRAM  administratively down down
========192.168.100.3=========
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down
Ethernet0/2                unassigned      YES NVRAM  administratively down down
Ethernet0/3                unassigned      YES NVRAM  administratively down down

"""
