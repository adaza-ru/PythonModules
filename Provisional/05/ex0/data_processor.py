import abc
from typing import Any


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._current_rank: int = 0

    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available to output")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Any) -> None:

        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._current_rank, str(item)))
                self._current_rank += 1
        else:
            self._storage.append((self._current_rank, str(data)))
            self._current_rank += 1


class TextProcessor(DataProcessor):

    pass


class LogProcessor(DataProcessor):

    pass


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    print("Trying to validate input '42': ", end="")
    print(NumericProcessor().validate(42))
    print("Trying to validate input 'Hello': ", end="")
    print(NumericProcessor().validate("Hello"))
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        NumericProcessor().ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    test_data: list[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {test_data}")
    np: NumericProcessor = NumericProcessor()
    np.ingest(test_data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = np.output()
        print(f"Numeric value {rank}: {value}")
