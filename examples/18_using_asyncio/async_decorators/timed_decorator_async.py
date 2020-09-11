import asyncio
from datetime import datetime
import netdev


device_params = {
    "device_type": "cisco_ios",
    "host": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}


def timecode(function):
    async def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = await function(*args, **kwargs)
        print(">>> Функция выполнялась:", datetime.now() - start_time)
        return result

    return wrapper


@timecode
async def connect_ssh(device, command):
    async with netdev.create(**device) as ssh:
        await asyncio.sleep(5)
        output = await ssh.send_command(command)
    return output


if __name__ == "__main__":
    print(asyncio.run(connect_ssh(device_params, "sh clock")))
