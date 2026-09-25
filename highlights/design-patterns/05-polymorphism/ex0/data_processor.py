import abc
import typing


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._current_rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available to output")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items: list[int | float] = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._current_rank, str(item)))
            self._current_rank += 1


class TextProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items: list[str] = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._current_rank, item))
            self._current_rank += 1


class LogProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all((
                isinstance(data.get("log_level"), str),
                isinstance(data.get("log_message"), str)
            ))
        if isinstance(data, list):
            return all(
                isinstance(x, dict) and all((
                    isinstance(x.get("log_level"), str),
                    isinstance(x.get("log_message"), str)
                ))
                for x in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items: list[dict[str, str]]
        items = data if isinstance(data, list) else [data]
        for item in items:
            log_str = f"{item['log_level']}: {item['log_message']}"
            self._storage.append((self._current_rank, log_str))
            self._current_rank += 1


if __name__ == "__main__":

    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")

    try:

        print(" Trying to validate input '42': ", end="")
        print(NumericProcessor().validate(42))
        print(" Trying to validate input 'Hello': ", end="")
        print(NumericProcessor().validate("Hello"))
        print(" Test invalid ingestion of string 'foo' "
              "without prior validation:")
        try:
            NumericProcessor().ingest("foo")
        except ValueError as e:
            print(f" Got exception: {e}")
        test_numeric: list[int] = [1, 2, 3, 4, 5]
        print(f" Processing data: {test_numeric}")
        np: NumericProcessor = NumericProcessor()
        np.ingest(test_numeric)
        print(" Extracting 3 values...")
        for _ in range(3):
            rank, value = np.output()
            print(f" Numeric value {rank}: {value}")

        print("\nTesting Text Processor...")
        print(" Trying to validate input '42': ", end="")
        print(TextProcessor().validate(42))
        test_text: list[str] = ["Hello", "Nexus", "World"]
        print(f" Processing data: {test_text}")
        tp: TextProcessor = TextProcessor()
        tp.ingest(test_text)
        print(" Extracting 1 value...")
        for _ in range(1):
            rank, value = tp.output()
            print(f" Text value {rank}: {value}")

        print("\nTesting Log Processor...")
        print(" Trying to validate input 'Hello': ", end="")
        print(LogProcessor().validate("Hello"))
        test_log: list[dict[str, str]] = [
            {"log_level": "NOTICE", "log_message": "Connection to server"},
            {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
        ]
        print(f" Processing data: {test_log}")
        tl: LogProcessor = LogProcessor()
        tl.ingest(test_log)
        print(" Extracting 2 values...")
        for _ in range(2):
            rank, value = tl.output()
            print(f" Log entry {rank}: {value}")

    except Exception as e:
        print(f"Error in __main__({type(e).__name__}): {e}")
