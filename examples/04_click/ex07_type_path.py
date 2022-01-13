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
@click.argument("command", type=click.Choice(["sh clock", "sh ip int br"]))
@click.option(
    "-f", "--devices-params", type=click.Path(exists=True), default="devices.yaml"
)
@click.option("-d", "--dest", type=click.Path())
def cli(devices_params, command, dest):
    """
    Отправить команду COMMAND на устройства из файла DEVICES-PARAMS
    """
    print(f"{devices_params=}")
    print(f"{dest=}")
    with open(devices_params) as f:
        devices = yaml.safe_load(f)
    result = send_command_to_devices(devices, command)
    with open(dest, "w") as f:
        yaml.dump(result, f)
    pprint(result)


if __name__ == "__main__":
    cli()

