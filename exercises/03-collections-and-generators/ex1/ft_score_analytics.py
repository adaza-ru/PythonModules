import sys


def main() -> None:
    scores: list[int] = []

    print("=== Player Score Analytics ===")

    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print("No scores provided.", end="")
        print(" Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    count: int = len(scores)
    total: int = sum(scores)
    average: float = total / count
    high: int = max(scores)
    low: int = min(scores)
    score_range: int = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
