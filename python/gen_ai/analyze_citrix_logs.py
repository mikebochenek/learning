"""Summarize latency and signal-strength readings from Citrix CSI logs."""

from __future__ import annotations

import argparse
import csv
import math
import re
import statistics
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DEFAULT_LOG_DIR = Path(r"C:\dev\data\citrix")
TIMESTAMP_FORMAT = "%m/%d/%Y %H:%M:%S"
RECORD_PATTERN = re.compile(
    r"^Timestamp:\s*(?P<timestamp>\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{2}:\d{2})"
    r"\s+\|\s*Latency\s+\(ms\):\s*(?P<latency>\d+(?:\.\d+)?)\s*ms\b"
    r".*?\|\s*Signal Strength\s+\(dBm\):\s*(?P<signal>-?\d+(?:\.\d+)?)\s*dBm\b"
)


@dataclass(frozen=True)
class Reading:
    timestamp: datetime
    latency_ms: float
    signal_dbm: float


def read_log(path: Path) -> tuple[list[Reading], int]:
    readings = []
    malformed_records = 0

    with path.open(encoding="utf-8-sig", errors="replace") as log_file:
        for line in log_file:
            if not line.startswith("Timestamp:"):
                continue

            match = RECORD_PATTERN.search(line)
            if match is None:
                malformed_records += 1
                continue

            readings.append(
                Reading(
                    timestamp=datetime.strptime(
                        match.group("timestamp"), TIMESTAMP_FORMAT
                    ),
                    latency_ms=float(match.group("latency")),
                    signal_dbm=float(match.group("signal")),
                )
            )

    return readings, malformed_records


def percentile_95(values: list[float]) -> float:
    ordered = sorted(values)
    return ordered[math.ceil(0.95 * len(ordered)) - 1]


def print_summary(results: list[tuple[Path, list[Reading]]]) -> None:
    headers = (
        "File",
        "Samples",
        "Latency avg",
        "p95",
        "max",
        "Signal weak",
        "avg",
        "strong",
    )
    rows = []
    for path, readings in results:
        latencies = [reading.latency_ms for reading in readings]
        signals = [reading.signal_dbm for reading in readings]
        rows.append(
            (
                path.name,
                str(len(readings)),
                f"{statistics.mean(latencies):.1f}",
                f"{percentile_95(latencies):.1f}",
                f"{max(latencies):.1f}",
                f"{min(signals):.1f}",
                f"{statistics.mean(signals):.1f}",
                f"{max(signals):.1f}",
            )
        )

    widths = [
        max(len(headers[index]), *(len(row[index]) for row in rows))
        for index in range(len(headers))
    ]
    print("Latency values are in ms; signal values are in dBm.")
    print(
        "  ".join(
            header.ljust(widths[index]) for index, header in enumerate(headers)
        )
    )
    print("  ".join("-" * width for width in widths))
    for row in rows:
        print(
            "  ".join(
                value.ljust(widths[index]) for index, value in enumerate(row)
            )
        )


def print_details(results: list[tuple[Path, list[Reading]]]) -> None:
    print("\nIndividual readings (latency in ms, signal in dBm):")
    print(f"{'File':<54}  {'Timestamp':<19}  {'Latency':>8}  {'Signal':>8}")
    for path, readings in results:
        for reading in readings:
            print(
                f"{path.name:<54}  "
                f"{reading.timestamp:%Y-%m-%d %H:%M:%S}  "
                f"{reading.latency_ms:>8.1f}  {reading.signal_dbm:>8.1f}"
            )


def write_csv(output_path: Path, results: list[tuple[Path, list[Reading]]]) -> None:
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(("file", "timestamp", "latency_ms", "signal_dbm"))
        for path, readings in results:
            for reading in readings:
                writer.writerow(
                    (
                        path.name,
                        reading.timestamp.isoformat(sep=" "),
                        reading.latency_ms,
                        reading.signal_dbm,
                    )
                )


def save_plot(
    output_path: Path, results: list[tuple[Path, list[Reading]]]
) -> None:
    try:
        import matplotlib.dates as mdates
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise SystemExit(
            "Plotting requires matplotlib. Install it with: "
            "python -m pip install matplotlib"
        ) from exc

    figure, (latency_axis, signal_axis) = plt.subplots(
        2, 1, sharex=True, figsize=(12, 8), layout="constrained"
    )
    for path, readings in results:
        readings.sort(key=lambda reading: reading.timestamp)
        timestamps = [reading.timestamp for reading in readings]
        latency_axis.plot(
            timestamps,
            [reading.latency_ms for reading in readings],
            label=path.stem,
        )
        signal_axis.plot(
            timestamps,
            [reading.signal_dbm for reading in readings],
            label=path.stem,
        )

    latency_axis.set_title("Citrix connection latency")
    latency_axis.set_ylabel("Latency (ms)")
    latency_axis.grid(True, alpha=0.3)
    latency_axis.legend(fontsize="small")

    signal_axis.set_title("Citrix signal strength")
    signal_axis.set_ylabel("Signal (dBm)")
    signal_axis.set_xlabel("Time")
    signal_axis.grid(True, alpha=0.3)
    signal_axis.legend(fontsize="small")
    signal_axis.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d %H:%M"))
    figure.savefig(output_path, dpi=150)
    plt.close(figure)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Summarize latency and signal-strength readings in Citrix CSI logs."
        )
    )
    parser.add_argument(
        "log_dir",
        nargs="?",
        type=Path,
        default=DEFAULT_LOG_DIR,
        help=f"directory containing .txt logs (default: {DEFAULT_LOG_DIR})",
    )
    parser.add_argument(
        "--details",
        action="store_true",
        help="print every timestamped latency and signal reading",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        metavar="FILE",
        help="write all parsed readings to a CSV file",
    )
    parser.add_argument(
        "--plot",
        nargs="?",
        const=Path("citrix_latency_signal.png"),
        type=Path,
        metavar="FILE",
        help="save a latency and signal graph (default: citrix_latency_signal.png)",
    )
    args = parser.parse_args()

    if not args.log_dir.is_dir():
        parser.error(f"log directory does not exist: {args.log_dir}")

    log_paths = sorted(args.log_dir.glob("*.txt"))
    if not log_paths:
        parser.error(f"no .txt log files found in: {args.log_dir}")

    results = []
    for path in log_paths:
        try:
            readings, malformed_records = read_log(path)
        except OSError as exc:
            parser.error(f"cannot read {path}: {exc}")

        if malformed_records:
            print(
                f"Warning: skipped {malformed_records} malformed timestamp "
                f"record(s) in {path.name}.",
                file=sys.stderr,
            )
        if readings:
            results.append((path, readings))
        else:
            print(
                f"Warning: no valid latency/signal readings in {path.name}.",
                file=sys.stderr,
            )

    if not results:
        parser.error("no valid timestamped latency/signal readings found")

    print_summary(results)
    if args.details:
        print_details(results)
    if args.csv:
        try:
            write_csv(args.csv, results)
        except OSError as exc:
            parser.error(f"cannot write CSV file {args.csv}: {exc}")
        print(f"\nCSV written to {args.csv}")
    if args.plot:
        try:
            save_plot(args.plot, results)
        except OSError as exc:
            parser.error(f"cannot save plot {args.plot}: {exc}")
        print(f"Plot written to {args.plot}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
