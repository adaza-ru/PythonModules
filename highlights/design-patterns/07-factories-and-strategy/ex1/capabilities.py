import abc


class HealCapability(abc.ABC):
    """Abstract capability for healing."""

    @abc.abstractmethod
    def heal(self) -> str:
        """Heals the creature or others."""
        pass


class TransformCapability(abc.ABC):
    """Abstract capability for transformation."""

    is_transformed: bool

    @abc.abstractmethod
    def transform(self) -> str:
        """Transforms the creature."""
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        """Reverts the creature to its original form."""
        pass
