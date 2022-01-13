import socket
import selectors


def accept(server_socket):
    client_socket, client_address = server_socket.accept()
    print(f"{client_socket=}")
    print(f"{client_address=}")
    selector.register(client_socket, selectors.EVENT_READ)


def read(client_socket):
    data = client_socket.recv(4096)
    print(f'{data=}')
    if b"close" in data:
        selector.unregister(client_socket)
        client_socket.close()
    else:
        client_socket.send(data.upper())


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 9000))
server_socket.listen()

selector = selectors.DefaultSelector()
print(f"{selector=}")
selector.register(server_socket, selectors.EVENT_READ)


while True:
    print("Waiting for event...")
    new_events = selector.select() # selector.select(timeout=3)
    for event, _ in new_events:
        event_socket = event.fileobj

        if event_socket is server_socket:
            accept(server_socket)
        else:
            read(event_socket)
