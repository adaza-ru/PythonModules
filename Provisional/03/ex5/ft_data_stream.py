import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Infinitely yields random player events."""
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = ["run", "eat", "sleep", "grab", "move",
                          "climb", "swim", "release", "use"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
        event_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    """Yields and removes elements from a list randomly until empty."""
    while event_list:
        idx: int = random.randrange(len(event_list))
        event: tuple[str, str] = event_list.pop(idx)
        yield event


def main() -> None:
    """Demonstrates infinite stream and random consumption."""
    print("=== Game Data Stream Processor ===")

    stream: Generator[tuple[str, str], None, None] = gen_event()
    name: str
    action: str
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    event_list: list[tuple[str, str]] = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
