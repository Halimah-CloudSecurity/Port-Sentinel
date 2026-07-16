import ssl
import socket

from config import DEFAULT_TIMEOUT


def get_certificate_info(target, port):

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

        certificate = secure_socket.getpeercert()

        secure_socket.close()

        return {

            "subject": certificate.get("subject"),
            "issuer": certificate.get("issuer"),
            "valid_from": certificate.get("notBefore"),
            "valid_until": certificate.get("notAfter")

        }

    except Exception:

        return None