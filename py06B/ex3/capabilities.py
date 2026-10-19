"""Transform capability, kept separate from the Creature hierarchy."""

import abc

from .creatures import Creature


class TransformCapability(abc.ABC):
    """An ability that lets an entity change its battle form."""

    def __init__(self) -> None:
        self._transformed = False

    @property
    def transformed(self) -> bool:
        """Tell whether the entity is currently transformed."""
        return self._transformed

    @abc.abstractmethod
    def transform(self) -> str:
        """Enter the transformed state and return a message."""

    @abc.abstractmethod
    def revert(self) -> str:
        """Leave the transformed state and return a message."""


class Shiftling(Creature, TransformCapability):
    """Base entity combining a Creature and the transform capability."""

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """Attack differently depending on the current form."""
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        """Shift into the sharper form."""
        self._transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        """Return to the normal form."""
        self._transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """Evolved entity combining a Creature and the transform capability."""

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """Attack differently depending on the current form."""
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        """Morph into the dragonic battle form."""
        self._transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        """Stabilize the creature back into its normal form."""
        self._transformed = False
        return f"{self.name} stabilizes its form."
