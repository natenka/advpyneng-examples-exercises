from netmiko import ConnectHandler
import yaml
from typing import Dict, Union, List, Any



def send_show_command(device: Dict[str, Union[str, int, bool]], command: str) -> str:
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result: str = ssh.send_command(command)
        prompt = ssh.find_prompt()
    return f"{prompt}{command}\n{result}\n"


def send_show_command_to_devices(
    devices: List[Dict[str, Union[str, int, bool]]], command: str
) -> Dict[str, str]:
    data = {}
    for device in devices:
        output = send_show_command(device, command)
        data[device["host"]] = output
    return data


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices: List[Dict[str, Union[str, int, bool]]] = yaml.safe_load(f)
    result = send_show_command_to_devices(devices, command)
    print(result)
