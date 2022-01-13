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
@click.option(
    "-f", "--devices-params", type=click.File("r"), default="devices.yaml"
)
@click.option("-d", "--dest", type=click.File("w"))
def cli(devices_params, command, dest):
    """
    Отправить команду COMMAND на устройства из файла DEVICES-PARAMS
    """
    print(f"{devices_params=}")
    print(f"{dest=}")
    devices = yaml.safe_load(devices_params)
    result = send_command_to_devices(devices, command)
    yaml.dump(result, dest)
    pprint(result)


if __name__ == "__main__":
    cli()

