from concurrent.futures import ThreadPoolExecutor

from scanner import scan_port
from config import MAX_WORKERS
from cli import get_arguments


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