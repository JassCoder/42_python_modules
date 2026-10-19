"""Exercise 3 - exercise the transform capability of an entity."""

from typing import Protocol

from ex3 import TransformCreatureFactory


class Transformable(Protocol):
    """Structural view of an entity that can transform and revert."""

    def describe(self) -> str:
        """Return a description of the entity."""
        ...

    def attack(self) -> str:
        """Return the entity's attack message."""
        ...

    def transform(self) -> str:
        """Transform the entity."""
        ...

    def revert(self) -> str:
        """Revert the entity."""
        ...


def showcase(creature: Transformable) -> None:
    """Describe, attack, transform, attack again and revert."""
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


def main() -> None:
    """Run the capability demonstration."""
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    print("base:")
    showcase(factory.create_base())

    print("evolved:")
    showcase(factory.create_evolved())


if __name__ == "__main__":
    main()
