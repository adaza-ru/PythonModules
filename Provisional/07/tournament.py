from typing import List, Tuple
from ex0.factory import FlameFactory, AquaFactory, CreatureFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    StrategyError
)


def run_tournament(
    name: str,
    opponents: List[Tuple[CreatureFactory, BattleStrategy]]
) -> None:
    """Executes a tournament round-robin style."""
    try:
        print(f"{name}")
        print("*** Tournament ***")
        print(f"{len(opponents)} opponents involved")

        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                print("\n* Battle *")

                fact1, strat1 = opponents[i]
                fact2, strat2 = opponents[j]

                c1 = fact1.create_base()
                c2 = fact2.create_base()

                print(c1.describe())
                print("vs.")
                print(c2.describe())
                print("now fight!")

                strat1.act(c1)
                strat2.act(c2)

    except StrategyError as e:
        print(f"Battle error, aborting tournament: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main() -> None:
    """Setup and run the examples from the subject."""

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    flame = FlameFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    run_tournament("Tournament 0 (basic)", [
        (flame, normal),
        (healing, defensive)
    ])
    print("")

    run_tournament("Tournament 1 (error)", [
        (flame, aggressive),
        (healing, defensive)
    ])
    print("")

    run_tournament("Tournament 2 (multiple)", [
        (AquaFactory(), normal),
        (healing, defensive),
        (transform, aggressive)
    ])


if __name__ == "__main__":
    main()
