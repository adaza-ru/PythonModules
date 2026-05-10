import abc
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(abc.ABC):
    """Abstract factory for creating creature families."""

    @abc.abstractmethod
    def create_base(self) -> Creature:
        """Creates the base form of the creature."""
        pass

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        """Creates the evolved form of the creature."""
        pass


class FlameFactory(CreatureFactory):
    """Concrete factory for the Flame family."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Concrete factory for the Aqua family."""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
