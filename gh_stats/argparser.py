import argparse
from typing import Sequence


def parser(argv: Sequence[str] | None = None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--verbose",
        help="Verbose output of operations",
        action="store_true",
    )

    parser.add_argument(
        "-f",
        "--flags",
        help="Display status of all flags for debugging purposes",
        action="store_true",
    )

    parser.add_argument(
        "-e",
        "--extend",
        help="Show more statistics",
        action="store_true",
    )

    parser.add_argument(
        "-u",
        "--username",
        help="Check a specific github account",
        default="",
    )

    return vars(parser.parse_args(argv))