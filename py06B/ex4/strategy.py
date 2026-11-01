from abc import ABC, abstractmethod
from ex3.creature import Creature
from ex3.capability import TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy cannot handle a creature."""
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, entity: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return True

    def act(self, entity: Creature) -> None:
        if not self.is_valid(entity):
            raise InvalidStrategyError("Invalid creature")
        print(entity.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature) -> None:
        if not self.is_valid(entity):
            raise InvalidStrategyError(
                f"Invalid Creature '{entity.name}' "
                "for this aggressive strategy"
            )

        if isinstance(entity, TransformCapability):
            print(entity.transform())
            print(entity.attack())
            print(entity.revert())
