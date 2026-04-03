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


def water_plant(plant_name: str) -> None:
    """Attempts to water a plant."""
    if plant_name != plant_name.capitalize():
        raise PlantError(plant_name,
                         f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    """
    Tests watering a list of plants, ensuring the system safely opens
    and closes using a finally block.
    """
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    """Entry point to run the watering tests."""
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(valid_plants)

    print("\nTesting invalid plants...")
    invalid_plants = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(invalid_plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
