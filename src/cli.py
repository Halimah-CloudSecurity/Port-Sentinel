import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description="PortSentinel - TCP Port Scanner"
    )

    parser.add_argument(
        "--target",
        required=True,
        help="Target IP address or hostname"
    )

    parser.add_argument(
        "--start-port",
        type=int,
        required=True,
        help="Starting port"
    )

    parser.add_argument(
        "--end-port",
        type=int,
        required=True,
        help="Ending port"
    )

    return parser.parse_args()