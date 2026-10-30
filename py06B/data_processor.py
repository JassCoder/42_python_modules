from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

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
        # *Handle empty storage
        if not self._pending:
            raise IndexError("output() called on empty storage")
        # *Remove the oldest item ->
        # *using pop() with index zero means oldest entry
        item = self._pending.pop(0)
        return item

    def _store(self, values: list[str]) -> None:
        for value in values:
            #  * Store each value with its current rank
            self._pending.append((self._next_rank, value))
            #  * Increase the rank for the next value
            self._next_rank += 1


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        # * Check if the input is a single integer or float
        if isinstance(data, (int, float)):
            return True
        # * Check if every element in the list is numeric
        if isinstance(data, list):
            return all(isinstance(xyz, (int, float)) for xyz in data)
        # * Reject unsupported data types
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        def __init__(self) -> None:
            self.items: list[str]