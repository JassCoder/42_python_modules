from abc import ABC, abstractmethod
from .capability import TransformCapability


class Creature(ABC):
    """Abstract base class for all creatures."""

    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Shifting(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shifting", "Normal")
        TransformCapability.__init__(self)
    
    def attack(self) -> str:
        if self.is_transformed:
            return "Shifting performs a Bossted strike!"
        return "Shifting attacks normally."
    
    def transform(self) -> str:
        self.is_transformed = True
        return "Shifting shifts into a sharper form"
    
    def revert(self) -> str:
        self.is_transformed = True
        return "Shifting returns to normal."

