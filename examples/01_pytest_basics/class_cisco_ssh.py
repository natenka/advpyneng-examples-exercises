import paramiko
import time
from pprint import pprint
import socket
import re


class CiscoSSH:
    def __init__(
        self,
        host,
        username,
        password,
        enable_pass,
        max_read=60000,
        pause=0.5,
    ):
        self.host = host
        self.username = username
        self.password = password
        self.max_read = max_read
        self.pause = pause

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=host,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
        )
        self._ssh = client.invoke_shell()
        self._ssh.settimeout(2)

        self._ssh.send("enable\n")
        self._ssh.send(f"{enable_pass}\n")
        time.sleep(self.pause)
        self._ssh.recv(self.max_read)
        self._ssh.send(f"terminal length 0\n")
        time.sleep(self.pause)
        read_output = self._ssh.recv(self.max_read).decode("utf-8")
        self.prompt = re.search(r"\S+#", read_output).group()

    def _read_until(self, line):
        command_output = ""
        self._ssh.settimeout(5)
        while True:
            try:
                time.sleep(self.pause)
                part = self._ssh.recv(self.max_read).decode("utf-8")
                command_output += part
                match_prompt = re.search(line, command_output)
                if match_prompt:
                    break
            except socket.timeout:
                break
        return command_output.replace("\r\n", "\n")

    def _read_until_config_prompt(self):
        hostname = self.prompt.split("#")[0]
        output = self._read_until(fr"{hostname}\(\S+\)#|{self.prompt}")
        return output

    def _read_until_prompt(self):
        output = self._read_until(self.prompt)
        return output

    def send_show_command(self, command):
        self._ssh.send(f"{command}\n")
        output = self._read_until_prompt()
        return output

    def send_config_command(self, commands):
        if type(commands) == str:
            commands = ["conf t", commands, "end"]
        else:
            commands = ["conf t", *commands, "end"]
        output = ""
        for cmd in commands:
            self._ssh.send(f"{cmd}\n")
            output += self._read_until_config_prompt()
        return output

    def close(self):
        self._ssh.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
