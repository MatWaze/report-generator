from abc import ABC, abstractmethod
from typing import Any

class Report(ABC):
    @abstractmethod
    def print_result_table(self, csv_data: list[dict[str, Any]]) -> None:
        pass