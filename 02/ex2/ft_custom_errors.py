class GardenError(Exception):
    def __init__(self, message="A garden error occurred."):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant="unknown"):
        self.plant = plant
        super().__init__(f"The {plant} plant is wilting!")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


def raise_plants(plant: str = "unknown") -> None:
    """x"""
    raise PlantError(plant)


def raise_water() -> None:
    """x"""
    raise WaterError()


def test_errors() -> None:
    """x"""
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise_plants("tomato")
    except PlantError as e:
        print("Caught PlantError:", e)
    print("\nTesting WaterError...")
    try:
        raise_water()
    except WaterError as e:
        print("Caught WaterError:", e)
    print("\nTesting catching all garden errors...")
    try:
        raise_plants("tomato")
    except GardenError as e:
        print("Caught a garden error:", e)
    try:
        raise_water()
    except GardenError as e:
        print("Caught a garden error:", e)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
