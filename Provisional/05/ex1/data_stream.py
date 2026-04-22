import abc
import typing


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._current_rank: int = 0
        self._name: str = "Data Processor"

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

    def __init__(self) -> None:
        super().__init__()
        self._name: str = "Numeric Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: typing.Any) -> None:

        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._current_rank, str(item)))
            self._current_rank += 1


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self._name: str = "Data Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: typing.Any) -> None:

        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._current_rank, item))
            self._current_rank += 1


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self._name: str = "Log Processor"

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

    def ingest(self, data: typing.Any) -> None:

        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            log_str = f"{item['log_level']}: {item['log_message']}"
            self._storage.append((self._current_rank, log_str))
            self._current_rank += 1


class DataStream():

    def __init__(self) -> None:

        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:

        if not any(isinstance(obj, type(proc))
                   for obj in self._processors):
            self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:

        for data in stream:
            for proc in self._processors:
                if proc.validate(data):
                    proc.ingest(data)
                    break
            else:
                print("DataStream error - Can't process element"
                      f" in stream:{data}")

    def print_processors_stats(self) -> None:

        print("== DataStream statistics ==")

        if len(self._processors) != 0:
            for proc in self._processors:
                print(
                    f"{proc._name}: total {proc._current_rank} items"
                    f" processed, remaining {len(proc._storage)} on processor"
                )
        else:
            print("No processor found, no data")
        print("")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    ds: DataStream = DataStream()
    ds.print_processors_stats()

    print("Registering Numeric Processor\n")
    np: NumericProcessor = NumericProcessor()
    ds.register_processor(np)

    data: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"}
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {data}")
    ds.process_stream(data)
    ds.print_processors_stats()

    print("Registering other data processors")
    tp: TextProcessor = TextProcessor()
    lp: LogProcessor = LogProcessor()
    ds.register_processor(tp)
    ds.register_processor(lp)

    print("Send the same batch again")
    ds.process_stream(data)
    ds.print_processors_stats()

    print("Consume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    np.output()
    np.output()
    np.output()
    tp.output()
    tp.output()
    lp.output()
    ds.print_processors_stats()
