import socket

from config import DEFAULT_TIMEOUT


def grab_banner(target, port):
    """
    Attempt to retrieve a service banner.

    Returns:
        Banner text as a string,
        or None if unavailable.
    """

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(DEFAULT_TIMEOUT)

        sock.connect((target, port))

        banner = sock.recv(1024).decode(errors="ignore").strip()

        sock.close()

        if banner:
            return banner

        return None

    except Exception:
        return None