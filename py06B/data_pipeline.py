"""Code Nexus - data pipeline with duck-typed export plugins."""

from typing import Any, Protocol

from data_processor import (
    DataProcessor,
    LogProcessor,
    NumericProcessor,
    TextProcessor,
)
from data_stream import DataStream as BaseDataStream


class ExportPlugin(Protocol):
    """Structural constraint for every export plugin."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Export processed items, each paired with its processing rank."""
        ...


class CSVPlugin:
    """Export processed items as comma-separated values."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Print the values of ``data`` as one CSV row."""
        print("CSV Output:")
        print(",".join(self._escape(value) for _, value in data))

    @staticmethod
    def _escape(value: str) -> str:
        """Quote a CSV field when it contains a delimiter or a quote."""
        if any(char in value for char in (',', '"', "\n", "\r")):
            return '"' + value.replace('"', '""') + '"'
        return value


class JSONPlugin:
    """Export processed items as a flat JSON object indexed by rank."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Print the values of ``data`` as a JSON object."""
        print("JSON Output:")
        members = ", ".join(
            f'"item_{rank}": "{self._escape(value)}"'
            for rank, value in data
        )
        print("{" + members + "}")

    @staticmethod
    def _escape(value: str) -> str:
        """Escape the characters that are special inside a JSON string."""
        return (
            value.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\n", "\\n")
            .replace("\r", "\\r")
            .replace("\t", "\\t")
        )


class DataStream(BaseDataStream):
    """Data stream that can also export processed items through plugins."""

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Consume up to ``nb`` items per processor and export them."""
        for processor in self.processors:
            self._export_from(processor, nb, plugin)

    @staticmethod
    def _export_from(
        processor: DataProcessor, nb: int, plugin: ExportPlugin
    ) -> None:
        """Export up to ``nb`` stored items from a single processor."""
        data: list[tuple[int, str]] = []
        for _ in range(nb):
            if processor.remaining == 0:
                break
            data.append(processor.output())
        plugin.process_output(data)


def main() -> None:
    """Run the Exercise 2 demonstration."""
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    print("Registering Processors")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    batch: list[Any] = [
        "Hello world ",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! "
             "Use ssh instead "},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVPlugin())
    stream.print_processors_stats()

    second_batch: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash "},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days ",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello ",
    ]
    print(f"Send another batch of data: {second_batch}")
    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
