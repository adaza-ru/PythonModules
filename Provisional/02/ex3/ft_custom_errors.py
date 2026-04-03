class GardenError(Exception):
    """Base exception for the garden ecosystem."""
    def __init__(self, message: str = "A garden error occurred.") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Raised when a specific plant has an issue."""
    def __init__(self, plant: str = "unknown",
                 message: str | None = None) -> None:
        self.plant = plant
        if message is None:
            if plant == "unknown":
                message = "Unknown plant error"
            else:
                message = f"The {plant} plant is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    """Raised when the water system fails."""
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def raise_plants(plant: str = "unknown") -> None:
    """Simulates a plant-related failure."""
    raise PlantError(plant)


def raise_water() -> None:
    """Simulates a water-related failure."""
    raise WaterError()


def test_errors() -> None:
    """Test suite for custom exceptions."""
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise_plants("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise_plants("tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise_water()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
