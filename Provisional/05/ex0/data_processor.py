from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: list[tuple[int, str]] = []
        self._next_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._queue:
            raise ValueError("No data available for output")
        return self._queue.pop(0)

    def _store(self, text: str) -> None:
        self._queue.append((self._next_rank, text))
        self._next_rank += 1


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True

        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)) or isinstance(item, bool):
                    return False
            return True

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._store(item)
        else:
            self._store(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if self._is_valid_log_dict(data):
            return True

        if isinstance(data, list):
            for item in data:
                if not self._is_valid_log_dict(item):
                    return False
            return True

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                self._store(self._format_log(item))
        else:
            self._store(self._format_log(data))

    def _is_valid_log_dict(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return False
        for key, value in data.items():
            if not isinstance(key, str) or not isinstance(value, str):
                return False
        return True

    def _format_log(self, item: dict[str, str]) -> str:
        level = item.get("log_level", "")
        message = item.get("log_message", "")
        return level + ": " + message


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Testing Numeric Processor...")
    print("Trying to validate input '42': " + str(numeric.validate(42)))
    print("Trying to validate input 'Hello': " + str(numeric.validate("Hello")))
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # type: ignore[arg-type]
    except Exception as e:
        print("Got exception: " + str(e))

    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        rank, value = numeric.output()
        print("Numeric value " + str(rank) + ": " + value)

    print("Testing Text Processor...")
    print("Trying to validate input '42': " + str(text.validate(42)))
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, value = text.output()
    print("Text value " + str(rank) + ": " + value)

    print("Testing Log Processor...")
    print("Trying to validate input 'Hello': " + str(log.validate("Hello")))
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print("Processing data: " + str(logs))
    log.ingest(logs)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print("Log entry " + str(rank) + ": " + value)