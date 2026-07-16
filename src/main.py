import sys
import time

from concurrent.futures import ThreadPoolExecutor

from scanner import scan_port
from banner import grab_banner
from service_detector import identify_service
from report import display_results, save_json_report
from cli import get_arguments
from resolver import resolve_target
from utils import log_info, log_error
from validator import validate_arguments
from certificate import get_certificate_info

from config import (
    HTTPS_PORTS,
    ENABLE_TLS_ANALYSIS
)


# Get command-line arguments
args = get_arguments()

# Validate user input
validate_arguments(args)

# Target to scan
target = args.target

# Resolve hostname
resolved_ip = resolve_target(target)

if not resolved_ip:

    log_error(
        "Failed to resolve the target hostname."
    )

    log_error(
        f"Target: {target}"
    )

    sys.exit()


log_info("Starting PortSentinel scan...")
log_info(f"Target: {target}")
log_info(f"Resolved IP: {resolved_ip}")


# Start timing
start_time = time.time()


# Port range
ports = list(

    range(
        args.start_port,
        args.end_port + 1
    )

)


log_info(

    f"Scanning ports "
    f"{args.start_port} "
    f"to {args.end_port}"

)


# Store scan results
results = []


# Multithreaded scanning
with ThreadPoolExecutor(
        max_workers=args.workers
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

            log_info(
                f"Port {port} OPEN"
            )

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

            # TLS Certificate Analysis
            certificate_info = None

            if (

                ENABLE_TLS_ANALYSIS
                and port in HTTPS_PORTS

            ):

                certificate_info = get_certificate_info(

                    target,
                    port

                )

            # Store results
            results.append(

                {

                    "port": port,
                    "service": service,
                    "banner": banner,
                    "certificate": certificate_info

                }

            )


# Calculate scan time
end_time = time.time()

scan_time = round(
    end_time - start_time,
    2
)


# Display results
log_info(
    "Generating scan summary..."
)

display_results(

    results,
    target,
    len(ports),
    scan_time

)


# Save JSON report
if results:

    log_info(
        "Saving JSON report..."
    )

    save_json_report(
        results
    )

else:

    log_info(
        "No open ports found. "
        "JSON report was not generated."
    )


log_info(
    "Scan completed successfully."
)