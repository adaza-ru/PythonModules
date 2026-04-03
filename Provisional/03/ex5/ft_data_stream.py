import random
from typing import Generator

def gen_event() -> Generator[tuple[str, str], None, None]:
    """Infinitely yields random player events."""
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release", "use"]
    while True:
        yield (random.choice(players), random.choice(actions)) [cite: 611]

def consume_event(event_list: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    """Yields and removes elements from a list randomly until empty."""
    while event_list:
        idx = random.randrange(len(event_list))
        event = event_list.pop(idx) [cite: 614]
        yield event

def main() -> None:
    """Demonstrates infinite stream and random consumption."""
    print("=== Game Data Stream Processor ===")
    
    # 1. Process 1000 events [cite: 612]
    stream = gen_event()
    for i in range(1000):
        name, action = next(stream)
        if i < 15 or i > 991: # Limiting output for readability [cite: 616, 617]
            print(f"Event {i}: Player {name} did action {action}")
        elif i == 15:
            print("[...]")

    # 2. Build a list of 10 events [cite: 613]
    event_list = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    # 3. Consume the list [cite: 615]
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}") [cite: 618]

if __name__ == "__main__":
    main()