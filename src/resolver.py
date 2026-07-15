import socket


def resolve_target(target):
    """
    Resolve a hostname into an IP address.

    Returns:
        IP address if successful.
        None if resolution fails.
    """

    try:

        ip_address = socket.gethostbyname(
            target
        )

        return ip_address

    except socket.gaierror:

        return None