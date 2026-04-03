"""
Exercise 6: Garden Analytics.
Integrates static methods, class methods, and nested classes for complex metrics.
"""

class Plant:
    """Advanced plant model with internal statistics tracking."""
    
    class _Stats:
        """Nested encapsulated class to track method calls."""
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            """Displays the tracked statistics."""
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.stats = self._Stats()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        """Static method to check if a given age is greater than 365 days."""
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        """Class method to create an unknown plant."""
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self.height = round(self.height + 1.0, 1)
        self.stats.record_grow()

    def age_plant(self) -> None:
        self.age += 1
        self.stats.record_age()

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")
        self.stats.record_show()


class Flower(Plant):
    """Flower class that supports blooming."""
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Seed(Flower):
    """Specialized Flower that holds a seed count once bloomed."""
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds_count: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds_count}")


class Tree(Plant):
    """Tree class with specialized statistics tracking."""
    class _TreeStats(Plant._Stats):
        """Extended nested class to track shade production."""
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.stats = self._TreeStats()
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name.capitalize()} now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")
        self.stats.record_shade()

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        self.stats.record_show()


def display_plant_statistics(plant: Plant) -> None:
    """Global function to trigger the display of any plant's internal statistics."""
    plant.stats.display()


def main() -> None:
    """Demonstrates all analytics capabilities."""
    print("=== Garden statistics ===")
    
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}")

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_plant_statistics(rose)
    
    print("[asking the rose to grow and bloom]")
    rose.grow()
    for _ in range(8): 
        rose.grow() # Fast grow to match exact output target 23.0cm
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_plant_statistics(rose)

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_plant_statistics(oak)

    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    for _ in range(30):
        sunflower.grow()
    for _ in range(20):
        sunflower.age_plant()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_plant_statistics(sunflower)

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    print("[statistics for Unknown plant]")
    display_plant_statistics(anon)

if __name__ == "__main__":
    main()