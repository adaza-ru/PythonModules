"""
Exercise 1: Garden Data Organizer.
Introduces the Plant class to manage data efficiently.
"""

class Plant:
    """A model representing a generic plant in the garden."""
    
    name: str
    height: float
    age: int

    def show(self) -> None:
        """Displays the plant's information."""
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

def main() -> None:
    """Test function to instantiate and show multiple plants."""
    print("=== Garden Plant Registry ===")
    
    plant1 = Plant()
    plant1.name = "rose"
    plant1.height = 25.0
    plant1.age = 30
    
    plant2 = Plant()
    plant2.name = "sunflower"
    plant2.height = 80.0
    plant2.age = 45
    
    plant3 = Plant()
    plant3.name = "cactus"
    plant3.height = 15.0
    plant3.age = 120

    plant1.show()
    plant2.show()
    plant3.show()

if __name__ == "__main__":
    main()