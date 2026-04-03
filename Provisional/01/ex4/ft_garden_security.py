"""
Exercise 4: Garden Security System.
Implements data protection through encapsulation and validation.
"""

class Plant:
    """A secure plant model with protected attributes and validation."""
    
    def __init__(self, name: str, height: float, age: int) -> None:
        """Initializes plant using secure setters to prevent bad initial data."""
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        
        # Try to set initial values safely
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        """Returns the protected height."""
        return self._height

    def set_height(self, height: float) -> None:
        """Safely updates height if positive, otherwise prints error."""
        if height < 0:
            print(f"{self._name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)

    def get_age(self) -> int:
        """Returns the protected age."""
        return self._age

    def set_age(self, age: int) -> None:
        """Safely updates age if positive, otherwise prints error."""
        if age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(age)

    def show(self) -> None:
        """Displays the plant's protected information."""
        print(f"{self._name.capitalize()}: {self._height}cm, {self._age} days old")

def main() -> None:
    """Demonstrates data validation and encapsulation."""
    print("=== Garden Security System ===")
    
    rose = Plant("rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()

    print("Height updated: 25cm")
    rose.set_height(25.0)
    
    print("Age updated: 30 days")
    rose.set_age(30)
    
    rose.set_height(-5.0)
    rose.set_age(-10)
    
    print("Current state: ", end="")
    rose.show()

if __name__ == "__main__":
    main()