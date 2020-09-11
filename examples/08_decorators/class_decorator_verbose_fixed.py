import paramiko
import time
from functools import wraps


def verbose(func):
    print("Декорируем функцию")

    @wraps(func)
    def inner(*args, **kwargs):
        if isinstance(args[0], BaseSSH):
            repr_args = ("self",) + args[1:]
        print(
            f"Вызываю функцию {func.__name__}, " f"args {repr_args}, kwargs {kwargs} "
        )
        return func(*args, **kwargs)

    return inner


def verbose_methods(cls):
    for name, value in vars(cls).items():
        if callable(value):
            setattr(cls, name, verbose(value))
    return cls


@verbose_methods
class BaseSSH:
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


if __name__ == "__main__":
    r1 = BaseSSH("192.168.100.1", "cisco", "cisco")
    r1.send_show_command(command="sh clock")
