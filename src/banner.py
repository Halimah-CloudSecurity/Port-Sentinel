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

    return "HTTP service detected (enumeration coming soon)"