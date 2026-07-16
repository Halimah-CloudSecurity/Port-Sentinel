import socket


def get_dns_information(target):

    dns_info = {

        "a_record": [],
        "cname": [],
        "mx_records": [],
        "name_servers": []

    }

    try:

        # A Records

        ip_address = socket.gethostbyname(target)

        dns_info["a_record"].append(
            ip_address
        )

    except Exception:

        pass

    try:

        # Canonical Name

        cname = socket.getfqdn(target)

        dns_info["cname"].append(
            cname
        )

    except Exception:

        pass

    try:

        # Name Servers

        import dns.resolver

        answers = dns.resolver.resolve(

            target,
            "NS"

        )

        for answer in answers:

            dns_info["name_servers"].append(

                str(answer)

            )

    except Exception:

        pass

    try:

        # MX Records

        import dns.resolver

        answers = dns.resolver.resolve(

            target,
            "MX"

        )

        for answer in answers:

            dns_info["mx_records"].append(

                str(answer.exchange)

            )

    except Exception:

        pass

    return dns_info