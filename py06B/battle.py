from ex3 import FlameFactory, TransformCreatureFactory
from ex3.factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base = factory.create_base()
    evolved = factory.create_evolved()

    for creature in (base, evolved):
        print(creature.describe())
        print(creature.attack())


def test_battle(
    first: CreatureFactory,
    second: CreatureFactory
) -> None:
    print("Testing battle")

    attacker = first.create_base()
    defender = second.create_base()

    print(attacker.describe())
    print("vs.")
    print(defender.describe())
    print("fight!")
    print(attacker.attack())
    print(defender.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    transform = TransformCreatureFactory()

    test_factory(flame)
    test_factory(transform)
    test_battle(flame, transform)
