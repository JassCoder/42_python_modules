"""Code Nexus - polymorphic data stream."""

from typing import Any

from data_processor import (
    DataProcessor,
    DataProcessorError,
    LogProcessor,
    NumericProcessor,
    TextProcessor,
)


class DataStream:
    """Route each element to the first processor able to handle it."""

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    @property
    def processors(self) -> tuple[DataProcessor, ...]:
        """Return the registered processors in registration order."""
        return tuple(self._processors)

    def register_processor(self, proc: DataProcessor) -> None:
        """Register a new data processor for this stream."""
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Analyse every element and send it to a suitable processor."""
        for element in stream:
            if not self._dispatch(element):
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def _dispatch(self, element: Any) -> bool:
        """Send one element to the first processor accepting it."""
        for processor in self._processors:
            if processor.validate(element):
                try:
                    processor.ingest(element)
                except DataProcessorError as error:
                    print(f"DataStream error - {error}")
                return True
        return False

    def print_processors_stats(self) -> None:
        """Print how many items each processor ingested and still holds."""
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for processor in self._processors:
            print(
                f"{processor.label}: "
                f"total {processor.total_processed} items processed, "
                f"remaining {processor.remaining} on processor"
            )


def main() -> None:
    """Run the Exercise 1 demonstration."""
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Registering Numeric Processor")
    stream.register_processor(numeric)

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

    print("Registering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    log.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
