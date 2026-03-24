from utils.median_coffee_report import MedianCoffeeReport
from utils.reader import Reader
from utils.table import resulting_table
import statistics
import pytest

@pytest.fixture
def reader_one_file():
    return Reader([ "tests/files/math.csv" ], MedianCoffeeReport() )

@pytest.fixture
def reader_multiple_files():
    return Reader(
        [ "tests/files/math.csv", "tests/files/physics.csv", "tests/files/programming.csv" ],
        MedianCoffeeReport())

def test_reader_correct_attributes(reader_one_file):
    assert len(reader_one_file._files) == 1
    assert isinstance(reader_one_file._report, MedianCoffeeReport)

def test_csv_data_not_none(reader_one_file):
    csv_data = reader_one_file._get_csvs()

    assert csv_data is not None

def test_table_valid(reader_one_file):
    csv_data = reader_one_file._get_csvs()
    table = resulting_table(csv_data, "student", "coffee_spent", statistics.median)

    assert len(table) == 15

    assert table[0][0] == "Иван Кузнецов"
    assert table[0][1] == 650

    assert table[len(table) - 1][0] == "Мария Соколова"
    assert table[len(table) - 1][1] == 120

    assert table[len(table) // 2][0] == "Артем Григорьев"
    assert table[len(table) // 2][1] == 390

def test_reader_correct_attributes_multiple_files(reader_multiple_files):
    assert len(reader_multiple_files._files) == 3
    assert isinstance(reader_multiple_files._report, MedianCoffeeReport)

def test_table_valid_multiple_files(reader_multiple_files):
    csv_data = reader_multiple_files._get_csvs()
    table = resulting_table(csv_data, "student", "coffee_spent", statistics.median)

    assert len(table) == 15

    assert table[0][0] == "Иван Кузнецов"
    assert table[0][1] == 700

    assert table[len(table) - 1][0] == "Мария Соколова"
    assert table[len(table) - 1][1] == 140

    assert table[len(table) // 2][0] == "Артем Григорьев"
    assert table[len(table) // 2][1] == 420

def test_table_valid_multiple_files_mean_function(reader_multiple_files):
    csv_data = reader_multiple_files._get_csvs()
    table = resulting_table(csv_data, "student", "coffee_spent", statistics.mean)

    assert len(table) == 15

    assert table[0][0] == "Иван Кузнецов"
    assert round(table[0][1]) == 708

    assert table[len(table) - 1][0] == "Мария Соколова"
    assert round(table[len(table) - 1][1]) == 142

    assert table[len(table) // 2][0] == "Артем Григорьев"
    assert round(table[len(table) // 2][1]) == 428

def test_table_valid_multiple_files_asc(reader_multiple_files):
    csv_data = reader_multiple_files._get_csvs()
    table = resulting_table(csv_data, "student", "coffee_spent", statistics.median, False)

    assert len(table) == 15

    assert table[0][0] == "Мария Соколова"
    assert table[0][1] == 140

    assert table[len(table) - 1][0] == "Иван Кузнецов"
    assert table[len(table) - 1][1] == 700

    assert table[len(table) // 2][0] == "Артем Григорьев"
    assert table[len(table) // 2][1] == 420

# different report test
def test_table_valid_multiple_files_student_sleep_hours(reader_multiple_files):
    csv_data = reader_multiple_files._get_csvs()
    table = resulting_table(csv_data, "student", "sleep_hours", statistics.median)

    assert len(table) == 15

    assert table[0][0] == "Мария Соколова"
    assert table[0][1] == 8

    assert table[len(table) - 1][0] == "Иван Кузнецов"
    assert table[len(table) - 1][1] == 2

    assert table[len(table) // 2][0] == "Артем Григорьев"
    assert table[len(table) // 2][1] == 4.5