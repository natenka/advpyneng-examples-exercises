from pprint import pprint
import asyncio
from itertools import repeat
import random
import yaml
import netdev
from datetime import datetime


async def connect_ssh(device, command):
    print(f'Подключаюсь к {device["host"]}')
    async with netdev.create(**device) as ssh:
        output = await ssh.send_command(command)
        #sl = random.choice([3, 8, 2, 1, 7])
        #print(f'Спим {sl} {device["host"]}')
        #await asyncio.sleep(sl)
        #if device["host"] == "192.168.100.2":
        #    raise ValueError
    print(f'Получен результат от {device["host"]}')
    return output


async def send_command_to_devices(devices, command):
    pending = [asyncio.create_task(connect_ssh(device, command))
               for device in devices]
    done_all = []
    while True:
        done, pending = await asyncio.wait(
            pending, return_when=asyncio.FIRST_EXCEPTION
        )
        print(f"\n DONE {datetime.now()}")
        pprint(done)
        #print("\n PENDING")
        #pprint(pending)
        done_all.extend(done)
        if not pending:
            break
    return done_all


if __name__ == "__main__":
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(send_command_to_devices(devices, "sh run"))
