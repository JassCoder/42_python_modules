from ex3 import TransformCreatureFactory
from ex3.creature import Creature
from ex3.capability import TransformCapability


def test_transform(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())

    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


if __name__ == "__main__":
    factory = TransformCreatureFactory()

    print("Testing Creature with transform capability")

    print("base:")
    test_transform(factory.create_base())

    print("evolved:")
    test_transform(factory.create_evolved())
