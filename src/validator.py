import sys

from utils import log_error

from config import (

    MIN_PORT,
    MAX_PORT,
    MIN_TIMEOUT,
    MAX_TIMEOUT,
    MIN_WORKERS,
    MAX_ALLOWED_WORKERS

)


def validate_arguments(args):

    # Port validation

    if not (

        MIN_PORT <= args.start_port <= MAX_PORT

    ):

        log_error(

            f"Start port must be between "
            f"{MIN_PORT} and {MAX_PORT}."

        )

        sys.exit()


    if not (

        MIN_PORT <= args.end_port <= MAX_PORT

    ):

        log_error(

            f"End port must be between "
            f"{MIN_PORT} and {MAX_PORT}."

        )

        sys.exit()


    if args.start_port > args.end_port:

        log_error(

            "Start port cannot be greater "
            "than end port."

        )

        sys.exit()


    # Timeout validation

    if not (

        MIN_TIMEOUT <= args.timeout <= MAX_TIMEOUT

    ):

        log_error(

            f"Timeout must be between "
            f"{MIN_TIMEOUT} and "
            f"{MAX_TIMEOUT} seconds."

        )

        sys.exit()


    # Worker validation

    if not (

        MIN_WORKERS <= args.workers <= MAX_ALLOWED_WORKERS

    ):

        log_error(

            f"Workers must be between "
            f"{MIN_WORKERS} and "
            f"{MAX_ALLOWED_WORKERS}."

        )

        sys.exit()