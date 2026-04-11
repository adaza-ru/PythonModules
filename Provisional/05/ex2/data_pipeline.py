from abc import ABC, abstractmethod
from typing import Any, Protocol


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

    def remaining(self) -> int:
        return len(self._queue)


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list[str] = []
        for _, value in data:
            values.append(value)
        print("CSV Output:")
        print(",".join(values))


class JsonExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        parts: list[str] = []
        for rank, value in data:
            key = "item_" + str(rank)
            escaped = self._json_escape(value)
            parts.append('"' + key + '": "' + escaped + '"')
        print("JSON Output:")
        print("{" + ", ".join(parts) + "}")

    def _json_escape(self, value: str) -> str:
        return value.replace("\\", "\\\\").replace('"', '\\"')


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        self._totals: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        self._totals[proc] = 0

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    before = proc.remaining()
                    proc.ingest(element)
                    after = proc.remaining()
                    self._totals[proc] += after - before
                    handled = True
                    break
            if not handled:
                print("DataStream error - Can't process element in stream: " + str(element))

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if nb <= 0:
            return
        for proc in self._processors:
            extracted: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining() == 0:
                    break
                extracted.append(proc.output())
            if extracted:
                plugin.process_output(extracted)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            total = self._totals.get(proc, 0)
            remaining = proc.remaining()
            print(
                name
                + ": total "
                + str(total)
                + " items processed, remaining "
                + str(remaining)
                + " on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    logs = LogProcessor()

    print("Registering Processors")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(logs)

    batch1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("Send first batch of data on stream: " + str(batch1))
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CsvExportPlugin())
    stream.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print("Send another batch of data: " + str(batch2))
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JsonExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()