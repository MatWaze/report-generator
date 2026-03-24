from utils.parse import csv_file, valid_report
from argparse import ArgumentTypeError
import pytest

def test_file_does_not_exist():
    with pytest.raises(ArgumentTypeError, match="tests/files/test does not exist or is not a file"):
        assert csv_file("tests/files/test")

def test_file_exists():
    assert csv_file("tests/files/test.csv")
    assert csv_file("tests/files/math.csv")

def test_file_not_csv():
    with pytest.raises(ArgumentTypeError, match="tests/files/not_csv is not a CSV file"):
        assert csv_file("tests/files/not_csv")

    with pytest.raises(ArgumentTypeError, match="tests/files/csv is not a CSV file"):
        assert csv_file("tests/files/csv")

    with pytest.raises(ArgumentTypeError, match="tests/files/csv.cs is not a CSV file"):
        assert csv_file("tests/files/csv.cs")

def test_valid_report_type():
    assert valid_report("median-coffee")

def test_invalid_report_type():
    with pytest.raises(ArgumentTypeError, match="class is not a valid report type"):
        assert valid_report("class")