import asyncio
from ex03_module_classmethod import CiscoSSH
from pprint import pprint


async def send_show(ip, username, password, commands):
    ssh = await CiscoSSH.connect(ip, username, password)
    all_output = ""
    for command in commands:
        output = await ssh.send_show_command(command)
        print(">>>", ssh.parse_output(output))
        all_output += output
    return all_output


async def send_commands_to_devices(ip_list, commands):
    coroutines = [send_show(ip, "cisco", "cisco", commands) for ip in ip_list]
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    cmds = ["sh clock", "sh run | i hostname"]
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    pprint(asyncio.run(send_commands_to_devices(ip_list, cmds)))
