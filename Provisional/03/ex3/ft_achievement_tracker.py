import random

ACHIEVEMENTS_LIST = [
    'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme',
    'Untouchable', 'Boss Slayer', 'Strategist', 'Unstoppable', 'Speed Runner',
    'Survivor', 'Treasure Hunter', 'First Steps', 'Sharp Mind', 'Hidden Path Finder'
]

def gen_player_achievements() -> set[str]:
    """
    Generates a random set of unique achievements from the master list.
    """
    # Pick between 5 and 10 achievements to ensure variety [cite: 595]
    count = random.randint(5, 10)
    return set(random.sample(ACHIEVEMENTS_LIST, count)) [cite: 591]

def main() -> None:
    """Tracks and compares achievements across multiple players."""
    print("=== Achievement Tracker System ===")
    
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }
    
    for name, achs in players.items():
        print(f"Player {name}: {achs}")

    # Set operations [cite: 589, 592]
    all_achs = set().union(*players.values())
    common_achs = set.intersection(*players.values())
    
    print(f"All distinct achievements: {all_achs}")
    print(f"Common achievements: {common_achs}")

    for name, achs in players.items():
        # Achievements only this player has
        others = set().union(*(v for k, v in players.items() if k != name))
        only_this = achs.difference(others)
        print(f"Only {name} has: {only_this}")
        
    for name, achs in players.items():
        # Achievements this player doesn't have yet
        missing = all_achs.difference(achs)
        print(f" {name} is missing: {missing}")

if __name__ == "__main__":
    main()