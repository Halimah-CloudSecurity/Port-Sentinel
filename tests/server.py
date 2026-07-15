import socket


HOST = "127.0.0.1"
PORT = 8000


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()


print(f"Server listening on {HOST}:{PORT}")


while True:

    client_socket, address = server.accept()

    print(f"Connection received from {address}")

    banner = "SSH-2.0-OpenSSH_9.6\n"

    client_socket.send(banner.encode())

    client_socket.close()