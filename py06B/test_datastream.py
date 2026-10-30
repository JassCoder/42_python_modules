from data_processor import NumericProcessor, TextProcessor, LogProcessor
from data_stream import DataStream

stream = DataStream()

numeric = NumericProcessor()
text = TextProcessor()
logs = LogProcessor()

stream.register_processor(numeric)
stream.register_processor(text)
stream.register_processor(logs)

stream.process_stream([
    42,
    "hello",
    3.14,
    {"level": "INFO", "message": "Started"},
    None
])

assert numeric.total_processed == 2
assert text.total_processed == 1
assert logs.total_processed == 1

stream.print_processors_stats()

print("EX1 integration tests passed")
