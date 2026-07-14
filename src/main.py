from concurrent.futures import ThreadPoolExecutor

from scanner import scan_port
from banner import grab_banner
from cli import get_arguments
from config import MAX_WORKERS


args = get_arguments()

target = args.target

ports = range(args.start_port, args.end_port + 1)


with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

    futures = [
        executor.submit(scan_port, target, port)
        for port in ports
    ]

    for future in futures:

        port, is_open = future.result()

        if is_open:

            print(f"[+] Port {port} OPEN")

            banner = grab_banner(target, port)

            if banner:

                print(f"    Banner: {banner}")