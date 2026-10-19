"""Exercise 4 - tournament driven by abstract battle strategies."""

from ex3 import (
    CreatureFactory,
    FlameFactory,
    TransformCreatureFactory,
)
from ex4 import (
    AggressiveStrategy,
    BattleStrategy,
    InvalidStrategyTarget,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def _strategy_label(strategy: BattleStrategy) -> str:
    """Return the short name of a strategy, without its suffix."""
    return type(strategy).__name__.removesuffix("Strategy")


def battle(opponents: list[Opponent]) -> None:
    """Make each opponent face every other opponent exactly once."""
    fighters = [
        (factory.create_base(), strategy)
        for factory, strategy in opponents
    ]
    print(
        "[ "
        + ", ".join(
            f"({creature.name}+{_strategy_label(strategy)})"
            for creature, strategy in fighters
        )
        + " ]"
    )
    print("*** Tournament ***")
    print(f"{len(fighters)} opponents involved")

    for index, (creature, strategy) in enumerate(fighters):
        for rival, rival_strategy in fighters[index + 1:]:
            print("* Battle *")
            print(creature.describe())
            print("vs.")
            print(rival.describe())
            print("now fight!")
            try:
                strategy.act(creature)
                rival_strategy.act(rival)
            except InvalidStrategyTarget as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    """Run both tournament demonstrations."""
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    print("Tournament 0 (basic)")
    battle([
        (flame_factory, NormalStrategy()),
        (transform_factory, AggressiveStrategy()),
    ])

    print("Tournament 1 (error)")
    battle([
        (transform_factory, AggressiveStrategy()),
        (flame_factory, AggressiveStrategy()),
    ])


if __name__ == "__main__":
    main()
