from pprint import pprint
import time
import yaml
from itertools import repeat
import paramiko
from concurrent.futures import ThreadPoolExecutor


def read_until_prompt(ssh, prompt="#"):
    result = ""
    while True:
        try:
            page = ssh.recv(1000).decode("ascii")
            time.sleep(0.2)
        except paramiko.ssh_exception.socket.timeout:
            break
        result += page
        if prompt in page:
            break
    return result


def connect_ssh(device, command):
    # print(f'Подключаюсь к {device["host"]}')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(
        hostname=device["host"],
        username=device["username"],
        password=device["password"],
        look_for_keys=False,
        allow_agent=False,
    )

    with client.invoke_shell() as ssh:
        ssh.send("enable\n")
        ssh.send("cisco\n")
        read_until_prompt(ssh)

        ssh.send("terminal length 0\n")
        read_until_prompt(ssh)

        ssh.send(command + "\n")
        output = read_until_prompt(ssh)
    return output


def send_command_to_devices(devices, command):
    with ThreadPoolExecutor(max_workers=30) as executor:
        result = list(executor.map(connect_ssh, devices, repeat(command)))
    return result


if __name__ == "__main__":
    with open("devices_long.yaml") as f:
        devices = yaml.safe_load(f)
    result = send_command_to_devices(devices, "sh run")
    print(len(result))
    # pprint(list(map(len, result)))
    # with open('testfile_sh_run_all_paramiko.txt', 'w') as f:
    #    f.write(result[0])
