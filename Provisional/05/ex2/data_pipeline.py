import abc
import typing


class ExportPlugin(typing.Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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
        self._name: str = "Text Processor"

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

        print("\n== DataStream statistics ==")

        if len(self._processors) != 0:
            for proc in self._processors:
                print(
                    f"{proc._name}: total {proc._current_rank} items"
                    f" processed, remaining {len(proc._storage)} on processor"
                )
        else:
            print("No processor found, no data")
        print("")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            collected = []
            for _ in range(nb):
                try:
                    collected.append(proc.output())
                except IndexError:
                    break
            if collected:
                plugin.process_output(collected)


class CsvPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        output = ",".join([item[1] for item in data])
        print(output)


class JsonPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        json_items = [f'"item_{item[0]}": "{item[1]}"' for item in data]
        output = "{" + ", ".join(json_items) + "}"
        print(output)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...")
    ds: DataStream = DataStream()
    ds.print_processors_stats()

    print("Registering Processors\n")
    np: NumericProcessor = NumericProcessor()
    ds.register_processor(np)
    tp: TextProcessor = TextProcessor()
    ds.register_processor(tp)
    lp: LogProcessor = LogProcessor()
    ds.register_processor(lp)

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

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin: CsvPlugin = CsvPlugin()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    data2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print(f"Send another batch of data: {data2}")
    ds.process_stream(data2)
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JsonPlugin())
    ds.print_processors_stats()
