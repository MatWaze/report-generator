from statistics import median
from typing import Any
from tabulate import tabulate
from utils.report import Report
from utils.table import resulting_table

class MedianCoffeeReport(Report):
    def print_result_table(self, csv_data: list[dict[str, Any]]) -> None:
        # other reports may have different headers, columns, or a function (median in this case)
        headers = [ "student", "median-coffee" ]
        result_table = resulting_table(csv_data, "student", "coffee_spent", median)

        print(tabulate(result_table, headers=headers, tablefmt="grid"))