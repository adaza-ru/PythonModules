from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    """Tests if a factory can create and interact with its creatures."""
    try:
        print("Testing factory")

        base_creature = factory.create_base()
        print(base_creature.describe())
        print(base_creature.attack())

        evolved_creature = factory.create_evolved()
        print(evolved_creature.describe())
        print(evolved_creature.attack())

    except Exception as e:
        print(f"An error occurred while testing the factory: {e}")


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    """Simulates a battle between the base creatures of two factories."""
    try:
        print("Testing battle")

        fighter1 = factory1.create_base()
        fighter2 = factory2.create_base()

        print(fighter1.describe())
        print(" vs.")
        print(fighter2.describe())
        print(" fight!")
        print(fighter1.attack())
        print(fighter2.attack())

    except Exception as e:
        print(f"An error occurred during the battle: {e}")


def main() -> None:
    """Main execution block."""
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()

        test_factory(flame_factory)
        print("")
        test_factory(aqua_factory)
        print("")
        test_battle(flame_factory, aqua_factory)

    except Exception as e:
        print(f"A critical error occurred: {e}")


if __name__ == "__main__":
    main()
