from scrapli import Scrapli
from scrapli.exceptions import ScrapliException, ScrapliCommandFailure
import yaml


def send_show(device, command):
    try:
        with Scrapli(**device) as ssh:
            reply = ssh.send_command(command)
            output = reply.result
            reply.raise_for_status()
        return output
    except ScrapliCommandFailure:
        raise
    except ScrapliException as error:
        print(error, device["host"])



if __name__ == '__main__':
    with open('devices_scrapli.yaml') as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]
    print(send_show(r1, "sh clck"))
