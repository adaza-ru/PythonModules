import random

def main() -> None:
    """Transforms player data using list and dictionary comprehensions."""
    print("=== Game Data Alchemist ===")
    
    initial_players: list[str] = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {initial_players}")
    
    # List Comprehensions [cite: 624, 630]
    all_capitalized = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_capitalized}")
    
    only_initially_caps = [name for name in initial_players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_initially_caps}")
    
    # Dictionary Comprehensions [cite: 625, 627]
    scores = {name: random.randint(1, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")
    
    avg_score = sum(scores.values()) / len(scores) if scores else 0.0
    print(f"Score average is {round(avg_score, 2)}") [cite: 628]
    
    high_scores = {name: score for name, score in scores.items() if score > avg_score}
    print(f"High scores: {high_scores}")

if __name__ == "__main__":
    main()