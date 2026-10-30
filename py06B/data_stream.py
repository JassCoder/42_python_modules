from data_processor import DataProcessor

class DataStream:
    
    def __init__(self) -> None:
        self._database: list[tuple[int, str]] = []
