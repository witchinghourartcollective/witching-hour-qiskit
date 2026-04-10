"""Console entrypoint for witching-hour-qiskit."""

from __future__ import annotations

import argparse

from .api import DEFAULT_DEVICE_ID, DEFAULT_SHOTS, list_devices, run_bell_state_job


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="witching-hour-qiskit",
        description="Minimal qBraid + Qiskit command line workflow.",
    )
    subcommands = parser.add_subparsers(dest="command", required=True)

    list_parser = subcommands.add_parser(
        "list-devices",
        help="List devices visible to the current qBraid account.",
    )
    list_parser.add_argument("--limit", type=int, default=10)

    run_parser = subcommands.add_parser(
        "run-bell",
        help="Submit a Bell-state circuit to a qBraid runtime device.",
    )
    run_parser.add_argument("--device-id", default=DEFAULT_DEVICE_ID)
    run_parser.add_argument("--shots", type=int, default=DEFAULT_SHOTS)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "list-devices":
        for device in list_devices(limit=args.limit):
            print(device)
        return 0

    if args.command == "run-bell":
        run_bell_state_job(device_id=args.device_id, shots=args.shots)
        return 0

    parser.error(f"Unsupported command: {args.command}")
    return 2
