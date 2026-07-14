def identify_service(banner):

    banner = banner.lower()

    if "ssh" in banner:
        return "SSH"

    elif "ftp" in banner:
        return "FTP"

    elif "smtp" in banner:
        return "SMTP"

    elif "apache" in banner:
        return "HTTP"

    elif "nginx" in banner:
        return "HTTP"

    else:
        return "Unknown Service"