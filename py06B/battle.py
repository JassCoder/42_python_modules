"""Exercise 3 - create entity families and make them fight."""

from ex3 import (
    CreatureFactory,
    FlameFactory,
    TransformCreatureFactory,
)


def test_factory(factory: CreatureFactory) -> None:
    """Create and exercise the base and evolved entity of a factory."""
    print("Testing factory")
    for creature in (factory.create_base(), factory.create_evolved()):
        print(creature.describe())
        print(creature.attack())


def battle(first: CreatureFactory, second: CreatureFactory) -> None:
    """Make the base entity of two factories fight."""
    print("Testing battle")
    left = first.create_base()
    right = second.create_base()
    print(left.describe())
    print("vs.")
    print(right.describe())
    print("fight!")
    print(left.attack())
    print(right.attack())


def main() -> None:
    """Run the Exercise 3 demonstration."""
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()
    test_factory(flame_factory)
    test_factory(transform_factory)
    battle(flame_factory, transform_factory)


if __name__ == "__main__":
    main()
