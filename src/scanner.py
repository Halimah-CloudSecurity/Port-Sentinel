import socket


def scan_port(target, port):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    scanner.close()

    return result == 0


target = "127.0.0.1"

ports = [22, 80, 443, 8000, 8080]


for port in ports:

    if scan_port(target, port):
        print(f"[+] {port} OPEN")

    else:
        print(f"[-] {port} CLOSED")