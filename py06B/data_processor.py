"""Code Nexus - abstract data processor hierarchy."""

import abc
from typing import Any


class DataProcessorError(Exception):
    """Raised when a data processor receives data it cannot handle."""


class DataProcessor(abc.ABC):
    """Common processing interface shared by every data processor."""

    label: str = "Data Processor"

    def __init__(self) -> None:
        self._pending: list[tuple[int, str]] = []
        self._next_rank: int = 0

    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        """Tell whether ``data`` is suitable for this processor."""

    @abc.abstractmethod
    def ingest(self, data: Any) -> None:
        """Ingest ``data`` and store it until it is extracted."""

    def output(self) -> tuple[int, str]:
        """Extract the oldest stored value and its processing rank."""
        if not self._pending:
            raise DataProcessorError(f"No data left in {self.label}")
        return self._pending.pop(0)

    @property
    def total_processed(self) -> int:
        """Return the number of values ingested since creation."""
        return self._next_rank

    @property
    def remaining(self) -> int:
        """Return the number of values waiting to be extracted."""
        return len(self._pending)

    def _store(self, values: list[str]) -> None:
        """Store values in ingestion order, each with a unique rank."""
        for value in values:
            self._pending.append((self._next_rank, value))
            self._next_rank += 1


class NumericProcessor(DataProcessor):
    """Processor for integers, floats and lists of both."""

    label = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        """Accept numbers and lists containing only numbers."""
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                not isinstance(item, bool)
                and isinstance(item, (int, float))
                for item in data
            )
        return False

    def ingest(  # type: ignore[override]
        self, data: int | float | list[int | float]
    ) -> None:
        """Convert numeric data into strings and store them."""
        if not self.validate(data):
            raise DataProcessorError("Improper numeric data")
        if isinstance(data, list):
            self._store([str(item) for item in data])
        else:
            self._store([str(data)])


class TextProcessor(DataProcessor):
    """Processor for strings and lists of strings."""

    label = "Text Processor"

    def validate(self, data: Any) -> bool:
        """Accept strings and lists containing only strings."""
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:  # type: ignore[override]
        """Store textual data as-is, one item at a time."""
        if not self.validate(data):
            raise DataProcessorError("Improper text data")
        if isinstance(data, list):
            self._store(data)
        else:
            self._store([data])


class LogProcessor(DataProcessor):
    """Processor for log entries and lists of log entries."""

    label = "Log Processor"

    @staticmethod
    def _is_log_entry(data: Any) -> bool:
        """Tell whether ``data`` is a dict of string key-value pairs."""
        if not isinstance(data, dict):
            return False
        return all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in data.items()
        )

    def validate(self, data: Any) -> bool:
        """Accept log entries and lists containing only log entries."""
        if self._is_log_entry(data):
            return True
        if isinstance(data, list):
            return all(self._is_log_entry(item) for item in data)
        return False

    def ingest(  # type: ignore[override]
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        """Format log entries as strings and store them."""
        if not self.validate(data):
            raise DataProcessorError("Improper log data")
        entries = data if isinstance(data, list) else [data]
        self._store([self._format_entry(entry) for entry in entries])

    @staticmethod
    def _format_entry(entry: dict[str, str]) -> str:
        """Build the ``level: message`` representation of a log entry."""
        return ": ".join(value.strip() for value in entry.values()).strip()


def main() -> None:
    """Run the Exercise 0 demonstration."""
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except DataProcessorError as error:
        print(f"Got exception: {error}")
    numeric_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    numeric.ingest(numeric_data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    print("Testing Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    print(f"Trying to validate input 'Hello': {text.validate('Hello')}")
    text_data: list[str] = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text.ingest(text_data)
    print("Extracting 1 value...")
    for _ in range(1):
        rank, value = text.output()
        print(f"Text value {rank}: {value}")

    print("Testing Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    log_data: list[dict[str, str]] = [
        {"log_level": "NOTICE", "log_message": "Connection to server "},
        {"log_level": "ERROR", "log_message": "Unauthorized access!! "},
    ]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
