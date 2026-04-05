import random


ACHIEVEMENTS_LIST: list[str] = [
    'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme',
    'Untouchable', 'Boss Slayer', 'Strategist', 'Unstoppable', 'Speed Runner',
    'Survivor', 'Treasure Hunter', 'First Steps', 'Sharp Mind',
    'Hidden Path Finder'
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(5, 8)
    return set(random.sample(ACHIEVEMENTS_LIST, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    players: list[tuple[str, set[str]]] = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements())
    ]

    for name, achs in players:
        print(f"Player {name}: {achs}")

    player_sets: list[set[str]] = [p[1] for p in players]

    all_achs: set[str] = set().union(*player_sets)
    common_achs: set[str] = set.intersection(*player_sets)

    print(f"\nAll distinct achievements: {all_achs}")
    print(f"\nCommon achievements: {common_achs}\n")

    for name, achs in players:
        others: set[str] = set().union(
            *(p[1] for p in players if p[0] != name)
        )
        only_this: set[str] = achs.difference(others)
        print(f"Only {name} has: {only_this}")

    print("")

    for name, achs in players:
        missing: set[str] = all_achs.difference(achs)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
