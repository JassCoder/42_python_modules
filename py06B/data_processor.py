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
            self._pending.append((self._next_rank, value))
            self._next_rank += 1
            #  * Append (Ranks , value ) to self._pending
            #  * Increament slef._next_rank by 1


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        # * here we are checking one value at once.
        if isinstance(data, (int, float)):
            return True
        # * here we are checking values at inside data using all()
        if isinstance(data, list):
            return all(isinstance(xyz, (int, float)) for xyz in data)
        # * if our f(x) not validate as numeric return False
        return False
