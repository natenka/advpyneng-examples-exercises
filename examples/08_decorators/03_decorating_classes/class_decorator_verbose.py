import paramiko
import time


def verbose(func):
    def inner(*args, **kwargs):
        print(f"Вызываю функцию {func.__name__}")
        print("Аргументы", args, kwargs)
        return func(*args, **kwargs)
    return inner


def verbose_methods(cls):
    for attr, value in vars(cls).items():
        if not attr.startswith("__") and callable(value):
            setattr(cls, attr, verbose(value))
    return cls


class BaseSSH:
    device_type = "cisco_ios"
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self._MAX_READ = 10000

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(
            hostname=ip,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
        )

        self._ssh = client.invoke_shell()
        time.sleep(1)
        self._ssh.recv(self._MAX_READ)

    def send_show_command(self, command):
        self._ssh.send(command + "\n")
        time.sleep(2)
        result = self._ssh.recv(self._MAX_READ).decode("ascii")
        return result

    @verbose
    def send_config_commands(self, commands):
        if isinstance(commands, str):
            commands = [commands]
        for command in commands:
            self._ssh.send(command + "\n")
            time.sleep(0.5)
        result = self._ssh.recv(self._MAX_READ).decode("ascii")
        return result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._ssh.close()

    def close(self):
        self._ssh.close()

    def __repr__(self):
        return f"BaseSSH(ip={self.ip})"


