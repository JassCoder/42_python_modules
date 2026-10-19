"""Abstract battle strategies used by the tournament."""

import abc

from ex3.capabilities import TransformCapability
from ex3.creatures import Creature


class InvalidStrategyTarget(Exception):
    """Raised when a strategy receives an entity it cannot handle."""


class BattleStrategy(abc.ABC):
    """An algorithm deciding how an entity fights."""

    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Tell whether ``creature`` is suitable for this strategy."""

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        """Make ``creature`` fight according to this strategy."""


class NormalStrategy(BattleStrategy):
    """Plain strategy suitable for any entity."""

    def is_valid(self, creature: Creature) -> bool:
        """Accept every creature."""
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        """Simply attack."""
        if not self.is_valid(creature):
            raise InvalidStrategyTarget(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Strategy reserved for entities with the transform capability."""

    def is_valid(self, creature: Creature) -> bool:
        """Accept only entities that can transform."""
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        """Transform, attack, then revert."""
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyTarget(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
