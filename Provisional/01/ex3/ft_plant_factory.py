"""
Exercise 3: Plant Factory.
Streamlines plant creation using a constructor.
"""

class Plant:
    """A model representing a plant initialized via constructor."""
    
    def __init__(self, name: str, height: float, age: int) -> None:
        """Initializes a new plant with immediate data."""
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        """Displays the plant's information."""
        print(f"Created: {self.name.capitalize()}: {self.height}cm, {self.age} days old")

def main() -> None:
    """Creates and displays multiple plants rapidly."""
    print("=== Plant Factory Output ===")
    
    plants = [
        Plant("rose", 25.0, 30),
        Plant("oak", 200.0, 365),
        Plant("cactus", 5.0, 90),
        Plant("sunflower", 80.0, 45),
        Plant("fern", 15.0, 120)
    ]

    for plant in plants:
        plant.show()

if __name__ == "__main__":
    main()