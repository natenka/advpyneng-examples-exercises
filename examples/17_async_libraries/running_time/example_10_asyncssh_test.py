from pprint import pprint
import asyncio
from itertools import repeat

import yaml
import asyncssh


async def connect_ssh(device, command):
    # print(f'Подключаюсь к {device["host"]}')
    ssh_coroutine = asyncssh.connect(**device)
    # так как нет встроенного таймаута, запускаем через wait_for
    ssh = await asyncio.wait_for(ssh_coroutine, timeout=10)
    writer, reader, stderr = await ssh.open_session(
        term_type="Dumb", term_size=(200, 24)
    )
    output = await reader.readuntil(">")
    writer.write("enable\n")
    output = await reader.readuntil("Password")
    writer.write("cisco\n")
    output = await reader.readuntil([">", "#"])
    writer.write("terminal length 0\n")
    output = await reader.readuntil("#")

    # print(f'Отправляю команду {command} на устройство {device["host"]}')
    writer.write(command + "\n")
    output = await reader.readuntil("#")
    ssh.close()
    return output


async def send_command_to_devices(devices, command):
    coroutines = map(connect_ssh, devices, repeat(command))
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    with open("devices_long.yaml") as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(send_command_to_devices(devices, "sh run"))
    print(len(result))
    # pprint(list(map(len, result)))
    # with open('testfile_sh_run_all_asyncssh.txt', 'w') as f:
    #    f.write(result[0])
