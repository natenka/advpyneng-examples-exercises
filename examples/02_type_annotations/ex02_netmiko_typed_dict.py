from pprint import pprint
from typing import Dict, Union, List, Any, TypedDict, Optional
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import yaml
import netmiko

# new in Python 3.8
class NetmikoParams(TypedDict, total=False):
    host: str
    username: str
    secret: str
    device_type: str
    timeout: int
    port: int


def send_show(device: NetmikoParams, command: str) -> str:
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        output: str = ssh.send_command(command)
        return output


def connect_devices(devices: List[NetmikoParams], command: str) -> Dict[str, str]:
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
