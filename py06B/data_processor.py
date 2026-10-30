"""Data processor abstractions and concrete text/numeric processors.

Each processor accepts input via `ingest`, queues it internally with a
monotonically increasing rank, and emits it oldest-first via `output`.
"""

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base for processors that queue data and emit it FIFO.

    Subclasses must implement `validate` (accept/reject raw input) and
    `ingest` (validate, normalise, pass to `_store`). The base class
    provides the queue, the rank counter, and the `output` drain method.
    """

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Return True if `data` is acceptable for this processor.

        Args:
            data: Candidate input of any type.

        Returns:
            True if `data` may be passed to `ingest`; False otherwise.
        """

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Validate `data` and enqueue it for later `output` calls.

        Args:
            data: Input to store. Must satisfy `validate`.

        Raises:
            ValueError: If `data` fails `validate`.
        """

    def __init__(self) -> None:
        """Initialise an empty pending queue and a zeroed rank counter."""
        self._pending: list[tuple[int, str]] = []
        self._next_rank: int = 0

    def output(self) -> tuple[int, str]:
        """Remove and return the oldest queued (rank, value) pair.

        Returns:
            The `(rank, value)` tuple with the lowest rank.

        Raises:
            IndexError: If the pending queue is empty.
        """
        # *Handle empty storage
        if not self._pending:
            raise IndexError("output() called on empty storage")
        # *Remove the oldest item ->
        # *using pop() with index zero means oldest entry
        item = self._pending.pop(0)
        return item

    def _store(self, values: list[str]) -> None:
        """Append each value to the queue with a fresh increasing rank.

        Ranks start at the current `_next_rank` and increment by one per
        value, so insertion order matches rank order.

        Args:
            values: Strings to enqueue. Already validated and normalised.
        """
        for value in values:
            # * Store each value with its current rank
            self._pending.append((self._next_rank, value))
            # * Increase the rank for the next value
            self._next_rank += 1


class NumericProcessor(DataProcessor):
    """Processor that accepts ints, floats, or lists thereof.

    Values are stringified before storage so the queue remains
    `list[tuple[int, str]]` as declared by the base class.
    """

    def validate(self, data: Any) -> bool:
        """Return True if `data` is a number or a list of numbers.

        Args:
            data: Candidate input.

        Returns:
            True for numeric scalars or lists whose elements are all
            numeric; False otherwise.
        """
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
        """Validate numeric input, stringify it, and enqueue it.

        Accepts either a single number or a list of numbers. A scalar
        is wrapped in a one-element list before storage.

        Args:
            data: A number or a list of numbers.

        Raises:
            ValueError: If `data` is not numeric (per `validate`).
        """
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
        """Return True if `data` is a string or a list of strings.

        Args:
            data: Candidate input.

        Returns:
            True for `str` scalars or lists whose elements are all
            `str`; False otherwise.
        """
        # ! checking a single string
        if isinstance(data, str):
            return True
        # ! checking a list containing only str
        if isinstance(data, list):
            return all(isinstance(xyz, str) for xyz in data)
        # ! Rejects anything else
        return False

    def ingest(self, data: str | list[str]) -> None:
        """Validate text input, normalise to a list, and enqueue it.

        A single string is wrapped in a one-element list; a list is
        passed through unchanged. (Never `list(data)` on a bare string
        — that would split it into characters.)

        Args:
            data: A string or a list of strings.

        Raises:
            ValueError: If `data` is not a string or list of strings.
        """
        # * validating...
        if not self.validate(data):
            raise ValueError("Innvalid Data")
        # * Normalize single input into a list
        values = [data] if isinstance(data, str) else data
        # * passing list to _store
        self._store(values)
