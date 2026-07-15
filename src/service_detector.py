def identify_service(banner):

    banner_lower = banner.lower()


    # Protocol detection

    if "ssh" in banner_lower:
        return "SSH"

    elif "ftp" in banner_lower:
        return "FTP"

    elif "smtp" in banner_lower:
        return "SMTP"

    elif "apache" in banner_lower:
        return "HTTP (Apache)"

    elif "nginx" in banner_lower:
        return "HTTP (Nginx)"

    elif "cloudflare" in banner_lower:
        return "HTTP (Cloudflare)"

    elif "microsoft-iis" in banner_lower:
        return "HTTP (Microsoft IIS)"

    elif "gunicorn" in banner_lower:
        return "HTTP (Gunicorn)"

    elif "uvicorn" in banner_lower:
        return "HTTP (Uvicorn)"

    elif "litespeed" in banner_lower:
        return "HTTP (LiteSpeed)"

    elif "http/" in banner_lower:
        return "HTTP"

    else:
        return "Unknown Service"