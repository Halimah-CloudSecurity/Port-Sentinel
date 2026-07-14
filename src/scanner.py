import socket
from concurrent.futures import ThreadPoolExecutor


def scan_port(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))
    scanner.close()

    return port, (result == 0)


target = "127.0.0.1"
ports = [22, 80, 443, 445, 3306, 8000, 8080]

with ThreadPoolExecutor(max_workers=50) as executor:
    futures = [executor.submit(scan_port, target, port) for port in ports]

    for future in futures:
        port, is_open = future.result()

        if is_open:
            print(f"[+] Port {port} OPEN")
        else:
            print(f"[-] Port {port} CLOSED")