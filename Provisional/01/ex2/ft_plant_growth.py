"""
Exercise 2: Plant Growth Simulator.
Adds dynamic behaviors to the Plant class.
"""

class Plant:
    """A plant model capable of growing and aging over time."""
    
    name: str
    height: float
    age: int

    def show(self) -> None:
        """Displays the plant's current information."""
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        """Increases the plant's height by a specific amount."""
        self.height = round(self.height + 0.8, 1)

    def age_plant(self) -> None:
        """Increases the plant's age by one day."""
        self.age += 1

def main() -> None:
    """Simulates a week of growth for a plant."""
    print("=== Garden Plant Growth ===")
    
    rose = Plant()
    rose.name = "rose"
    rose.height = 25.0
    rose.age = 30

    start_height: float = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.show()
        if day < 7:
            rose.grow()
            rose.age_plant()

    growth: float = round(rose.height - start_height, 1)
    print(f"Growth this week: {growth}cm")

if __name__ == "__main__":
    main()