import random


def main() -> None:
    """Transforms player data using list and dictionary comprehensions."""
    print("=== Game Data Alchemist ===\n")

    initial_players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
        'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {initial_players}")

    all_capitalized: list[str] = [
        name.capitalize() for name in initial_players
    ]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_initially_caps: list[str] = [
        name for name in initial_players if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {only_initially_caps}")

    scores: dict[str, int] = {
        name: random.randint(1, 1000) for name in all_capitalized
    }
    print(f"\nScore dict: {scores}")

    avg_score: float = sum(scores.values()) / len(scores) if scores else 0.0
    print(f"Score average is {round(avg_score, 2)}")

    high_scores: dict[str, int] = {
        name: score for name, score in scores.items() if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
