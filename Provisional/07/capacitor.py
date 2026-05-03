from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing() -> None:
    """Tests healing capability lifecycle."""
    try:
        print("Testing Creature with healing capability")
        factory = HealingCreatureFactory()

        print("base:")
        base = factory.create_base()
        print(base.describe())
        print(base.attack())
        heal_method = getattr(base, "heal", None)
        if callable(heal_method):
            print(heal_method())

        print("evolved:")
        evolved = factory.create_evolved()
        print(evolved.describe())
        print(evolved.attack())
        heal_method_evolved = getattr(evolved, "heal", None)
        if callable(heal_method_evolved):
            print(heal_method_evolved())

    except Exception as e:
        print(f"An error occurred while testing healing capability: {e}")


def test_transform() -> None:
    """Tests transform capability lifecycle."""
    try:
        print("Testing Creature with transform capability")
        factory = TransformCreatureFactory()

        print("base:")
        base = factory.create_base()
        print(base.describe())
        print(base.attack())
        
        transform_method = getattr(base, "transform", None)
        if callable(transform_method):
            print(transform_method())
            
        print(base.attack())
        
        revert_method = getattr(base, "revert", None)
        if callable(revert_method):
            print(revert_method())

        print("evolved:")
        evolved = factory.create_evolved()
        print(evolved.describe())
        print(evolved.attack())
        
        transform_method_evolved = getattr(evolved, "transform", None)
        if callable(transform_method_evolved):
            print(transform_method_evolved())
            
        print(evolved.attack())
        
        revert_method_evolved = getattr(evolved, "revert", None)
        if callable(revert_method_evolved):
            print(revert_method_evolved())

    except Exception as e:
        print(f"An error occurred while testing transform capability: {e}")


def main() -> None:
    """Main execution block."""
    try:
        test_healing()
        test_transform()
    except Exception as e:
        print(f"A critical error occurred: {e}")


if __name__ == "__main__":
    main()
