import abc
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class StrategyError(Exception):
    """Exception raised when a strategy is incompatible with a creature."""
    pass


class BattleStrategy(abc.ABC):
    """Abstract base class for battle strategies."""

    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Checks if the creature is compatible with this strategy."""
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        """Executes the strategy actions."""
        pass


class NormalStrategy(BattleStrategy):
    """Strategy for standard attacks, compatible with all creatures."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Strategy for transformable creatures: Transform -> Attack -> Revert."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )

        transform = getattr(creature, "transform")
        revert = getattr(creature, "revert")
        
        print(transform())
        print(creature.attack())
        print(revert())


class DefensiveStrategy(BattleStrategy):
    """Strategy for healing creatures: Attack -> Heal."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )

        heal = getattr(creature, "heal")
 
        print(creature.attack())
        print(heal())
