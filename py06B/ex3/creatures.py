"""Entity hierarchy of the Code Nexus combat sandbox."""

import abc


class Creature(abc.ABC):
    """An entity with a name, a type and an attack behaviour."""

    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abc.abstractmethod
    def attack(self) -> str:
        """Return the message describing this creature's attack."""

    def describe(self) -> str:
        """Return a standard description of this creature."""
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    """Base entity of the fire family."""

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        """Return the Flameling attack message."""
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """Evolved entity of the fire family."""

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        """Return the Pyrodon attack message."""
        return f"{self.name} uses Flamethrower!"
