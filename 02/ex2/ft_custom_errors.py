class GardenError(Exception):
    """x"""

    def __str__(self):
        """x"""
        return "A garden error ocurred."


class PlantError(GardenError):
    """x"""

    def __str__(self):
        """x"""
        return f"The {self.args[0]} plant is wilting!"


class WaterError(GardenError):
    """x"""

    def __str__(self):
        """x"""
        return "Not enough water in the tank!"


def raise_plants() -> None:
    """x"""
    pass


def raise_water() -> None:
    """x"""
    pass


def test_errors() -> None:
    """x"""
    pass
    

if __name__ == "__main__":
    test_errors()

"""
Authorized: print(), int(), input()


Create functions that:
• Raise your custom errors in different situations
• Show how to catch your specific error types
• Demonstrate that catching GardenError catches all garden-related errors


Example:
=== Custom Garden Errors Demo ===
Testing PlantError...
Caught PlantError: The tomato plant is wilting!
Testing WaterError...
Caught WaterError: Not enough water in the tank!
Testing catching all garden errors...
Caught a garden error: The tomato plant is wilting!
Caught a garden error: Not enough water in the tank!
All custom error types work correctly!
"""