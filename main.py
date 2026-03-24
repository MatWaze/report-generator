from utils.median_coffee_report import MedianCoffeeReport
from utils.reader import Reader
from utils.parse import csv_file
from utils.parse import valid_report
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', type=csv_file, help='List of .csv files')
    parser.add_argument('--report', type=valid_report, help='Report to display')

    args = parser.parse_args()

    # each report has its own report strategy class
    if args.report == "median-coffee":
        report = MedianCoffeeReport()

    reader = Reader(args.files, report)
    reader.show_report()

if __name__ == "__main__":
    main()