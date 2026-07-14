import socket

from config import DEFAULT_TIMEOUT


def scan_port(target, port):
    """
    Scan a single TCP port.

    Returns:
        (port, True) if open
        (port, False) if closed
    """

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(DEFAULT_TIMEOUT)

    result = scanner.connect_ex((target, port))

    scanner.close()

    return port, (result == 0) 