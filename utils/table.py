from typing import Any, Callable

def get_columns(
    csv_data: list[dict[str, Any]],
    first_column: str,
    second_column: str
) -> dict[str, list[Any]]:
    dictionary : dict[str, list[Any]] = {}

    for line in csv_data:
        key = line[first_column]
        value = float(line[second_column])

        if key not in dictionary:
            dictionary[key] = []

        dictionary[key].append(value)
    
    return dictionary

# params: csv dictionary data, first column to read from, second column, aggregate function, and boolean descending or not
def resulting_table(
    csv_data: list[dict[str, Any]],
    first_column: str,
    second_column: str,
    criteria: Callable[[list[Any]], Any],
    desc: bool=True
) -> list[list[Any]]:
    dictionary = get_columns(csv_data, first_column, second_column)

    result_table: list[list[Any]] = []

    for (key, val) in dictionary.items():
        med: float = criteria(val)
        result_table.append([key, med])

    result_table.sort(key=lambda row: (row[1]), reverse=desc)

    return result_table