from pprint import pprint
import asyncio
from itertools import repeat

import yaml
import netdev


async def connect_ssh(device, command):
    # print(f'Подключаюсь к {device["host"]}')

    async with netdev.create(**device) as ssh:
        output = await ssh.send_command(command)
    return output


async def send_command_to_devices(devices, command):
    coroutines = map(connect_ssh, devices, repeat(command))
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(send_command_to_devices(devices, "sh run"))
    print(len(result))
    # pprint(list(map(len, result)))
    # with open('testfile_sh_run_all_asyncssh.txt', 'w') as f:
    #    f.write(result[0])
