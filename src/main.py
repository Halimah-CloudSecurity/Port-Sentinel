from concurrent.futures import ThreadPoolExecutor

from scanner import scan_port
from banner import grab_banner
from service_detector import identify_service
from report import display_results
from cli import get_arguments
from config import MAX_WORKERS


args = get_arguments()

target = args.target

ports = range(args.start_port, args.end_port + 1)

results = []


with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

    futures = [

        executor.submit(scan_port, target, port)

        for port in ports
    ]


    for future in futures:

        port, is_open = future.result()

        if is_open:

            banner = grab_banner(target, port)

            if banner:

                service = identify_service(banner)

            else:

                banner = "No banner found"

                service = "Unknown"


            result = {

                "port": port,
                "service": service,
                "banner": banner

            }

            results.append(result)


display_results(results)
print(f"\nTotal Open Ports : {len(results)}")