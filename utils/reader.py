from pathlib import Path
from typing import Any
from tabulate import tabulate
from statistics import median
from utils.report import Report
from utils.table import resulting_table
import csv

class Reader:
    def __init__(self, files: list[Path], report: Report):
        self._files = files
        self._report = report

    def _get_csvs(self) -> list[dict[str, Any]]:
        csv_data: list[dict[str, Any]] = []

        for file in self._files:
            with open(file, "r", encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                csv_data.extend(csv_reader)

        return csv_data

    def show_report(self) -> None:
        self._report.print_result_table(self._get_csvs())