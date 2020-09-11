import asyncio
import random
import asyncssh
import aiofiles


async def connect_ssh(ip, command, username="cisco", password="cisco"):
    print(f"Подключаюсь к {ip}")
    ssh_coroutine = asyncssh.connect(ip, username=username, password=password)
    # так как нет встроенного таймаута, запускаем через wait_for
    ssh = await asyncio.wait_for(ssh_coroutine, timeout=10)
    writer, reader, stderr = await ssh.open_session(
        term_type="Dumb", term_size=(200, 24)
    )
    output = await reader.readuntil(">")
    writer.write("enable\n")
    output = await reader.readuntil("Password")
    writer.write("cisco\n")
    output = await reader.readuntil("#")
    writer.write("terminal length 0\n")
    output = await reader.readuntil("#")

    print(f"Отправляю команду {command} на устройство {ip}")
    writer.write(command + "\n")
    output = await reader.readuntil([">", "#"])
    ssh.close()
    return ip, command, output


async def write_to_file(data):
    ip, command, text = data
    filename = f"{ip.replace('.', '_')}_{command}.txt"
    print(f"Записываю в файл {filename} данные")
    async with aiofiles.open(filename, "w") as f:
        await f.write(text)
    print("Done")


async def main():
    command = "sh clock"
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    coroutines = [connect_ssh(ip, command) for ip in ip_list]
    tasks = []
    for f in asyncio.as_completed(coroutines):
        try:
            output = await f
            tasks.append(asyncio.create_task(write_to_file(output)))
        except Exception as exc:
            print("Исключение", exc)
    print(">>> Ждем выполнения всех задач")
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
