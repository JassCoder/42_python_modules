"""Functional tests for the data processor classes."""

from typing import Any

from data_processor import NumericProcessor, TextProcessor, LogProcessor


# NumericProcessor — ingest and drain FIFO
numeric = NumericProcessor()
numeric.ingest([10, 2.5, 30])
assert numeric.output() == (0, "10")
assert numeric.output() == (1, "2.5")
assert numeric.output() == (2, "30")

# TextProcessor — ingest and drain FIFO
text = TextProcessor()
text.ingest(["hello", "world"])
assert text.output() == (0, "hello")
assert text.output() == (1, "world")

# LogProcessor — one dict becomes one string with one rank
logs = LogProcessor()
logs.ingest({"level": "INFO", "message": "Started"})
assert logs.output() == (0, "level=INFO, message=Started")

# NumericProcessor — rejects invalid input
# Pass via `Any` so mypy doesn't flag the deliberate type mismatch.
bad: Any = "invalid"
try:
    numeric.ingest(bad)
except ValueError:
    print("Invalid numeric input correctly rejected")
else:
    raise AssertionError("Invalid input was accepted")

print("EX0 functional tests passed")
