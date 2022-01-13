import telnetlib
import time
import random
from concurrent.futures import ThreadPoolExecutor


def client(client_id):
    telnet = telnetlib.Telnet('127.0.0.1', port=9000)
    telnet.write(str(client_id).encode() + b"\r\n")
    time.sleep(random.random())
    print(f"{telnet.read_very_eager()=}")

    telnet.write(str(client_id).encode() + b"\r\n")
    time.sleep(random.random())
    print(f"## {telnet.read_very_eager()=}")
    telnet.write(b'close\r\n')



with ThreadPoolExecutor(10) as ex:
    futures = [ex.submit(client, i) for i in range(1, 11)]
    [f.result() for f in futures]
