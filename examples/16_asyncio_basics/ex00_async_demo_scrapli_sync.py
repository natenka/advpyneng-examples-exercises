from pprint import pprint
from concurrent.futures import ThreadPoolExecutor

import yaml
from scrapli import Scrapli
from scrapli.exceptions import ScrapliException


def send_show(device, show_command):
    try:
        with Scrapli(**device) as ssh:
            reply = ssh.send_command(show_command)
            return reply.result
    except ScrapliException as error:
        print(error, device["host"])


def send_command_to_devices(devices, command):
    result_dict = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_list = [executor.submit(send_show, dev, command) for dev in devices]
        for dev, f in zip(devices, future_list):
            result_dict[dev["host"]] = f.result()
    return result_dict


if __name__ == "__main__":
    with open("devices_sync.yaml") as f:
        devices = yaml.safe_load(f)
    result = send_command_to_devices(devices, "sh ip int br")
    pprint(result, width=120)
