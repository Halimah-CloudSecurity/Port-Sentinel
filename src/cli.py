import argparse

from config import (
    START_PORT,
    END_PORT,
    MAX_WORKERS,
    DEFAULT_TIMEOUT
)


def get_arguments():

    parser = argparse.ArgumentParser(

        description=(
            "PortSentinel - Lightweight "
            "Reconnaissance Framework"
        )

    )

    parser.add_argument(

        "--target",
        required=True,
        help="Target hostname or IP address"

    )

    parser.add_argument(

        "--start-port",
        type=int,
        default=START_PORT,
        help=f"Starting port (default: {START_PORT})"

    )

    parser.add_argument(

        "--end-port",
        type=int,
        default=END_PORT,
        help=f"Ending port (default: {END_PORT})"

    )

    parser.add_argument(

        "--workers",
        type=int,
        default=MAX_WORKERS,
        help=f"Maximum worker threads (default: {MAX_WORKERS})"

    )

    parser.add_argument(

        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Connection timeout in seconds (default: {DEFAULT_TIMEOUT})"

    )

    parser.add_argument(

        "--version",
        action="version",
        version="PortSentinel v1.0"

    )

    return parser.parse_args()