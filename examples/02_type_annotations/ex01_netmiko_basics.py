from pprint import pprint
from typing import Dict, Union, List, Any
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import yaml
import netmiko

DictStrAny = Dict[str, Union[str, int, float, bool]]


def send_show(device: DictStrAny, command: str) -> str:
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        output: str = ssh.send_command(command)
        return output


def connect_devices(devices: List[DictStrAny], command: str) -> Dict[Any, str]:
    results = {}
    with ThreadPoolExecutor() as ex:
        results_map = ex.map(send_show, devices, repeat(command))
        for dev, out in zip(devices, results_map):
            results[dev["host"]] = out
    return results


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        output = send_show(dev, "sh clock")
        pprint(output, width=120)
