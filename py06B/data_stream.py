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

    def print_processor_stats(self) -> None:
        for processor in self._processors:
            print(type(processor).__name__)
            print(processor._next_rank)
            print(len(processor._pending))
