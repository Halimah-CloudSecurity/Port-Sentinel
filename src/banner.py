import socket

from config import DEFAULT_TIMEOUT


def grab_banner(target, port):

    """
    Retrieve service information
    based on protocol behavior.
    """

    if port in [80, 8080]:

        return grab_http_banner(target, port)

    return grab_standard_banner(target, port)


def grab_standard_banner(target, port):

    try:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(DEFAULT_TIMEOUT)

        sock.connect((target, port))

        banner = sock.recv(1024).decode(
            errors="ignore"
        ).strip()

        sock.close()

        if banner:
            return banner

        return None

    except Exception:
        return None


def grab_http_banner(target, port):

    """
    Placeholder for HTTP support.
    """

def grab_http_banner(target, port):

    try:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(DEFAULT_TIMEOUT)

        sock.connect((target, port))

        http_request = (
            f"GET / HTTP/1.1\r\n"
            f"Host: {target}\r\n"
            f"Connection: close\r\n\r\n"
        )

        sock.send(http_request.encode())

        response = sock.recv(4096).decode(
            errors="ignore"
        )

        sock.close()

        lines = response.splitlines()

        if not lines:
            return None

        return "\n".join(lines[:5])

    except Exception:

        return None