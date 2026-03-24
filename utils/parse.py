from argparse import ArgumentTypeError
from pathlib import Path

report_types = [ "median-coffee" ]

def csv_file(value: str) -> Path:
    path = Path(value)

    if not path.is_file():
        raise ArgumentTypeError(f"{value} does not exist or is not a file")

    if path.suffix.lower() != ".csv":
        raise ArgumentTypeError(f"{value} is not a CSV file")

    return path.resolve()

def valid_report(value: str):
    if value not in report_types:
        raise ArgumentTypeError(f"{value} is not a valid report type")
    
    return value
