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
        # ! Handle empty storage
        if not self._pending:
            raise IndexError("output() called on empty storage")
        # ! Remove the oldest item ->
        # ! using pop() with index zero means oldest entry
        item = self._pending.pop(0)
        return item

    
