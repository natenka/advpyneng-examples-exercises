import asyncio


async def ping(ip):
    reply = await asyncio.create_subprocess_shell(
        f"ping -c 3 -n {ip}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await reply.communicate()

    ip_is_reachable = reply.returncode == 0
    return ip_is_reachable


async def ping_ip_list(ip_list):
    coroutines = [ping(ip) for ip in ip_list]
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3", "192.168.100.11"]
    results = asyncio.run(ping_ip_list(ip_list))
    print(results)
