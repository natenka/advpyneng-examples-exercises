import asyncssh
from asyncssh.encryption import get_encryption_algs


async def send_config_commands(
    host, username, password, enable_password, config_commands
):
    encryption_algs = [enc.decode("ascii") for enc in get_encryption_algs()]
    ssh_coroutine = asyncssh.connect(
        host,
        username=username,
        password=password,
        encryption_algs=encryption_algs,
        known_hosts=None,  # Accept any key
    )
    pass
