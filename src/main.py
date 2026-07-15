import time

from concurrent.futures import ThreadPoolExecutor

from scanner import scan_port
from banner import grab_banner
from service_detector import identify_service
from report import display_results, save_json_report
from cli import get_arguments
from config import MAX_WORKERS
from utils import log_info


# Get command-line arguments
args = get_arguments()


# Target to scan
target = args.target

log_info("Starting PortSentinel scan...")
log_info(f"Target: {target}")


# Start timing the scan
start_time = time.time()


# Create the port range
ports = range(
    args.start_port,
    args.end_port + 1
)

log_info(
    f"Scanning ports {args.start_port} to {args.end_port}"
)


# Store scan results
results = []


# Create a thread pool for faster scanning
with ThreadPoolExecutor(
        max_workers=MAX_WORKERS
) as executor:

    futures = [

        executor.submit(
            scan_port,
            target,
            port
        )

        for port in ports

    ]


    for future in futures:

        port, is_open = future.result()

        if is_open:

            log_info(f"Port {port} OPEN")

            banner = grab_banner(
                target,
                port
            )

            if banner:

                service = identify_service(
                    banner
                )

            else:

                banner = "No banner found"
                service = "Unknown"

            result = {

                "port": port,
                "service": service,
                "banner": banner

            }

            results.append(result)


# Calculate scan time
end_time = time.time()

scan_time = round(
    end_time - start_time,
    2
)


log_info("Generating scan summary...")


# Display results
display_results(

    results,
    target,
    len(ports),
    scan_time

)


# Save report only if useful
if results:

    log_info("Saving JSON report...")
    save_json_report(results)

else:

    log_info(
        "No open ports found. JSON report was not generated."
    )


log_info("Scan completed successfully.")