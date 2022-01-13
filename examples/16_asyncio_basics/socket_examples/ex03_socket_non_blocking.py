import socket
import time


def accept(server_socket):
    client_socket, client_address = server_socket.accept()
    client_socket.setblocking(False) # non-blocking
    print(f"{client_socket=}")
    print(f"{client_address=}")
    client_sockets_list.append(client_socket)


def read(client_socket):
    data = client_socket.recv(4096)
    print(f'{data=}')
    client_socket.send(data.upper())
    if b"close" in data:
        client_socket.close()
        client_sockets_list.remove(client_socket)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setblocking(False) # non-blocking
server_socket.bind(("localhost", 9000))
server_socket.listen()
client_sockets_list = []


while True:
    try:
        accept(server_socket)
    except BlockingIOError:
        pass
    for cl_socket in client_sockets_list:
        try:
            read(cl_socket)
        except BlockingIOError:
            pass
    time.sleep(1)
    print("Waiting...")
