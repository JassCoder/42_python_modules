from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base for processors that queue data and emit it FIFO."""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def __init__(self) -> None:
        self._pending: list[tuple[int, str]] = []
        self._next_rank: int = 0

    def output(self) -> tuple[int, str]:
        # * Handle empty storage
        if not self._pending:
            raise IndexError("output() called on empty storage")
        # * Remove the oldest item ->
        # * using pop() with index zero means oldest entry
        item = self._pending.pop(0)
        return item

    def _store(self, values: list[str]) -> None:
        for value in values:
            # * Store each value with its current rank
            self._pending.append((self._next_rank, value))
            # * Increase the rank for the next value
            self._next_rank += 1


class NumericProcessor(DataProcessor):
    """Processor that accepts ints, floats, or lists thereof."""

    def validate(self, data: Any) -> bool:
        # * Check if the input is a single integer or float
        if isinstance(data, (int, float)):
            return True
        # * Check if every element in the list is numeric
        if isinstance(data, list):
            return all(
                isinstance(xyz, (int, float)) for xyz in data
            )
        # * Reject unsupported data types
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid Numeric input")
        # * checking data is in list or not
        if isinstance(data, list):
            numbers = data
        else:
            numbers = [data]
        converted = [str(item) for item in numbers]
        self._store(converted)


class TextProcessor(DataProcessor):
    """Processor that accepts strings or lists of strings."""

    # ? Validition
    def validate(self, data: Any) -> bool:
        # * checking a single string
        if isinstance(data, str):
            return True
        # * checking a list containing only str
        if isinstance(data, list):
            return all(isinstance(xyz, str) for xyz in data)
        # * Rejects anything else
        return False

    def ingest(self, data: str | list[str]) -> None:
        # * validating...
        if not self.validate(data):
            raise ValueError("Innvalid Data")
        # * Normalize single input into a list
        values = [data] if isinstance(data, str) else data
        # * passing list to _store
        self._store(values)

class LogProcessor(DataProcessor):
    """Processor that accepts dicts with str keys and str values."""

    def _is_log_entry(self, entry: Any) -> bool:
        if not isinstance(entry, dict):
            return False
        return all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in entry.items()
            )
    
    def validate(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return self._is_log_entry(data)
        
        if not isinstance(data , list):
            return all(self._is_log_entry(item) for item in data)
        
        return False
        
    def ingest(self, data: Any) -> None:
        pass