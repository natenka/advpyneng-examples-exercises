import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(("localhost", 9000))
server_socket.listen()


try:
    print("Waiting accept...")
    client_socket, client_address = server_socket.accept()
    print(f"{client_socket=}")
    print(f"{client_address=}")

    client_data = b""

    while b"\n" not in client_data:
        data = client_socket.recv(1)
        print(f'{data=}')
        client_data += data
    print(f"{client_data=}")

    client_socket.send(client_data.upper())
    client_socket.close()
finally:
    server_socket.close()
