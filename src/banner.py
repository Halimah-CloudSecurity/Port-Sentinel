import socket
import ssl

from config import DEFAULT_TIMEOUT


SECURITY_HEADERS = [

    "Strict-Transport-Security",

    "Content-Security-Policy",

    "X-Frame-Options",

    "X-Content-Type-Options",

    "Permissions-Policy"

]


def grab_banner(target, port):
    """
    Retrieve service information
    based on protocol behavior.
    """

    if port in [80, 8080]:
        return grab_http_banner(target, port)

    if port == 443:
        return grab_https_banner(target, port)
    
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

        banner = "\n".join(lines[:5])

        found, missing = analyze_security_headers(
            response
        )

        if found:

            banner += "\n\nSecurity Headers Found:"

            for header in found:

                banner += f"\n- {header}"

        if missing:

            banner += "\n\nMissing Security Headers:"

            for header in missing:

                banner += f"\n- {header}"

        return banner

    except Exception:

        return None


def analyze_security_headers(response):

    found_headers = []

    missing_headers = []

    for header in SECURITY_HEADERS:

        if header.lower() in response.lower():

            found_headers.append(header)

        else:

            missing_headers.append(header)

    return found_headers, missing_headers 

def grab_https_banner(target, port):

    try:

        context = ssl.create_default_context()

        sock = socket.create_connection(
            (target, port),
            timeout=DEFAULT_TIMEOUT
        )

        secure_socket = context.wrap_socket(
            sock,
            server_hostname=target
        )

        https_request = (
            f"GET / HTTP/1.1\r\n"
            f"Host: {target}\r\n"
            f"Connection: close\r\n\r\n"
        )

        secure_socket.send(
            https_request.encode()
        )

        response = secure_socket.recv(
            4096
        ).decode(errors="ignore")

        secure_socket.close()

        lines = response.splitlines()

        if not lines:
            return None

        banner = "\n".join(lines[:5])

        found, missing = analyze_security_headers(
            response
        )

        if found:

            banner += "\n\nSecurity Headers Found:"

            for header in found:

                banner += f"\n- {header}"

        if missing:

            banner += "\n\nMissing Security Headers:"

            for header in missing:

                banner += f"\n- {header}"

        return banner

    except Exception:

        return None