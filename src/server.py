import socket

# Create a TCP IPv4 socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind it to localhost on port 8000
server_socket.bind(("127.0.0.1", 8000))

# Listen for incoming connections
server_socket.listen()

print("Server is listening on 127.0.0.1:8000...")

while True:
    # Wait for a client
    client_socket, address = server_socket.accept()

    print(f"\n[+] Client connected: {address}")

    # Receive data
    message = client_socket.recv(1024).decode()

    print(f"Client says: {message}")

    # Send a reply
    reply = "Welcome to PortSentinel!"
    client_socket.send(reply.encode())

    # Close this client's connection
    client_socket.close()

    print("[+] Client disconnected") 