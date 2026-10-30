"""Plugin interface and CSV exporter for (rank, value) streams."""
from typing import Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvPlugin:
    """Exports (rank, value) pairs as a single comma-separated line."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _rank, value in data]
        csv_line = ",".join(values)
        print("CSV Output:")
        print(csv_line)


class JsonPlugin:
    """Exports (rank, value) pairs as a JSON array of objects."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        records = [
            f'{{"rank": {rank}, "value": "{_escape(value)}"}}'
            for rank, value in data
        ]
        json_text = "[" + ", ".join(records) + "]"
        print("JSON Output:")
        print(json_text)


if __name__ == "__main__":
    sample = [(0, "apple"), (1, "banana"), (2, "orange")]
    CsvPlugin().process_output(sample)
