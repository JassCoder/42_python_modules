from typing import Any
from data_processor import DataProcessor


class DataStream:

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, processor: DataProcessor) -> None:
        self._processors.append(processor)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for processor in self._processors:
                if processor.validate(element):
                    try:
                        processor.ingest(element)
                    except ValueError as error:
                        print(f"Ingestion error: {error}")
                    break
            else:
                print(f"No processor accepted: {element!r}")

    def print_processors_stats(self) -> None:
        for processor in self._processors:
            print(type(processor).__name__)
            print(processor.total_processed)
            print(processor.remaining)


if __name__ == "__main__":
    from data_processor import NumericProcessor, TextProcessor, LogProcessor

    print("=== Code Nexus - Data Stream ===")

    stream = DataStream()
    numeric = NumericProcessor()
    text = TextProcessor()
    logs = LogProcessor()

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(logs)

    stream.process_stream([
        "Hello world",
        [3.14, -1, 2.71],
        {"log_level": "INFO", "log_message": "Connected"},
        42,
        ["Hi", "five"]
    ])

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    numeric.output()
    text.output()
    logs.output()

    print("== DataStream statistics ==")
    stream.print_processors_stats()
