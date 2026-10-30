from typing import Protocol


data = [(0, "apple"), (1, "banana"), (2, "orange")]


class CsvPlugin:
    """Exports (rank, value) pairs as a single comma-separated line."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _rank, value in data]
        csv_line = ", ".join(values)
        print("CSV out:")
        print(csv_line)
        
        
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


if __name__ == "__main__":
    sample = [(0, "apple"), (1, "banana"), (2, "orange")]
    CsvPlugin().process_output(sample)