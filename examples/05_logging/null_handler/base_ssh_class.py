import paramiko
import time
import logging

# Logging configuration
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


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
        log.debug(f"Подключение к {self.ip}")
        time.sleep(1)
        self._ssh.recv(self._MAX_READ)

    def send_show_command(self, command):
        log.debug(f"Отправка команды {command} на {self.ip}")
        self._ssh.send(command + "\n")
        time.sleep(2)
        result = self._ssh.recv(self._MAX_READ).decode("ascii")
        return result

    def send_config_commands(self, commands):
        log.debug(f"Отправка команд {commands} на {self.ip}")
        if isinstance(commands, str):
            commands = [commands]
        for command in commands:
            self._ssh.send(command + "\n")
            time.sleep(0.5)
        result = self._ssh.recv(self._MAX_READ).decode("ascii")
        return result

    def __enter__(self):
        log.debug(f"Метод __enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        log.debug(f"Метод __exit__")
        self._ssh.close()

    def close(self):
        self._ssh.close()
