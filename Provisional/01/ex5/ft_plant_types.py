"""
Exercise 5: Specialized Plant Types.
Demonstrates class inheritance and method overriding using super().
"""

class Plant:
    """Base class for all plant types."""
    
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def grow(self) -> None:
        self.height = round(self.height + 1.0, 1)

    def age_plant(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    """A specialized plant that has a color and can bloom."""
    
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        """Makes the flower bloom."""
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    """A specialized plant that provides shade."""
    
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        """Calculates and prints the shade produced by the tree."""
        print(f"Tree {self.name.capitalize()} now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    """A specialized plant that provides nutritional value over time."""
    
    def __init__(self, name: str, height: float, age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 5

    def age_plant(self) -> None:
        super().age_plant()
        self.nutritional_value += 2

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    """Tests the behavior of specialized plant types."""
    print("=== Garden Plant Types ===")
    
    print("\n=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age_plant()
    tomato.show()

if __name__ == "__main__":
    main()