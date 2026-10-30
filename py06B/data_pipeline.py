from typing import Protocol


data = [(0, "apple"), (1, "banana"), (2, "orange")]


class CsvPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = []
        
        for rank, value in data:
            values.append(value)
        
        csv_line = ", ".join(values)
        print("CSV out:")
        print(csv_line)
        
        
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        