"""Plugin interface and CSV exporter for (rank, value) streams."""
from typing import Protocol
from data_stream import DataStream as BaseDataStream


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


def escape_csv(value: str) -> str:
    if any(char in value for char in ',\"\n\r'):
        return '"' + value.replace('"', '""') + '"'
    return value


def escape_json(value: str) -> str:
    result = ""

    for char in value:
        code = ord(char)

        if char == '"':
            result += '\\"'
        elif char == "\\":
            result += "\\\\"
        elif char == "\n":
            result += "\\n"
        elif char == "\r":
            result += "\\r"
        elif char == "\t":
            result += "\\t"
        elif code < 32:
            result += f"\\u{code:04x}"
        else:
            result += char

    return result


class CsvPlugin:
    """Exports (rank, value) pairs as a single comma-separated line."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [escape_csv(value) for _rank, value in data]
        csv_line = ",".join(values)
        print("CSV Output:")
        print(csv_line)


class JsonPlugin:
    """Exports (rank, value) pairs as a JSON object."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        records = [
            f'"item_{rank}": "{escape_json(value)}"'
            for rank, value in data
        ]

        json_text = "{" + ", ".join(records) + "}"

        print("JSON Output:")
        print(json_text)


class DataStream(BaseDataStream):
    """Extends EX1 DataStream with an output pipeline."""

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if nb < 0:
            raise ValueError("nb cannot be negative")

        for processor in self._processors:
            results: list[tuple[int, str]] = []

            for _ in range(nb):
                try:
                    results.append(processor.output())
                except IndexError:
                    break

            plugin.process_output(results)


if __name__ == "__main__":
    from data_processor import NumericProcessor, TextProcessor, LogProcessor

    stream = DataStream()

    numeric = NumericProcessor()
    text = TextProcessor()
    logs = LogProcessor()

    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(logs)

    stream.process_stream([
        42,
        3.14,
        "hello",
        "world",
        {"level": "INFO", "message": "started"}
    ])

    print("=== Before export ===")
    stream.print_processors_stats()

    print("=== CSV Export ===")
    stream.output_pipeline(2, CsvPlugin())

    print("=== After CSV ===")
    stream.print_processors_stats()

    print("=== JSON Export ===")
    stream.process_stream([100, "Python", 200])
    stream.output_pipeline(2, JsonPlugin())

    print("=== Final statistics ===")
    stream.print_processors_stats()
