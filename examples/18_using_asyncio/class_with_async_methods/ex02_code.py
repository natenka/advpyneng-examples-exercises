import asyncio
from ex02_module_with import CiscoSSH
from pprint import pprint


async def send_show(ip, username, password, commands):
    async with CiscoSSH(ip, username, password) as ssh:
        output = ""
        for command in commands:
            output += await ssh.send_show_command(command)
    return output


async def send_commands_to_devices(ip_list, commands):
    coroutines = [send_show(ip, "cisco", "cisco", commands) for ip in ip_list]
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    cmds = ["sh clock", "sh run | i hostname"]
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    pprint(asyncio.run(send_commands_to_devices(ip_list, cmds)))
