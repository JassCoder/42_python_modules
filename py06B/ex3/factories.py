"""Abstract factory used to create entities without exposing their classes."""

import abc

from .capabilities import Morphagon, Shiftling
from .creatures import Creature, Flameling, Pyrodon


class CreatureFactory(abc.ABC):
    """Create the base and evolved entity of one family."""

    @abc.abstractmethod
    def create_base(self) -> Creature:
        """Create the base entity of the family."""

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved entity of the family."""


class FlameFactory(CreatureFactory):
    """Factory for the fire family."""

    def create_base(self) -> Flameling:
        """Create a Flameling."""
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        """Create a Pyrodon."""
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    """Factory for the transforming family."""

    def create_base(self) -> Shiftling:
        """Create a Shiftling."""
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        """Create a Morphagon."""
        return Morphagon()
