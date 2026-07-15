import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wait at most 1 second for operations
client_socket.settimeout(1)

client_socket.connect(("127.0.0.1", 8000))

client_socket.send("Hello from Black X!".encode())

reply = client_socket.recv(1024).decode()

print(reply)

client_socket.close()