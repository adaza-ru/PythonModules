import abc


class Creature(abc.ABC):
    """Abstract base class for all creatures."""

    def __init__(self, name: str, creature_type: str) -> None:
        self.name: str = name
        self.creature_type: str = creature_type

    @abc.abstractmethod
    def attack(self) -> str:
        """Abstract method for a creature's attack."""
        pass

    def describe(self) -> str:
        """Returns a generic description of the creature."""
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    """Concrete base creature for Flame family."""

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    """Concrete evolved creature for Flame family."""

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    """Concrete base creature for Aqua family."""

    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    """Concrete evolved creature for Aqua family."""

    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"