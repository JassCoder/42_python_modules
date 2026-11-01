from ex3 import FlameFactory, TransformCreatureFactory
from ex3.factory import CreatureFactory
from ex4 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)


def tournament(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            first_factory, first_strategy = opponents[i]
            second_factory, second_strategy = opponents[j]

            first = first_factory.create_base()
            second = second_factory.create_base()

            print("* Battle *")
            print(first.describe())
            print("vs.")
            print(second.describe())
            print("now fight!")

            try:
                first_strategy.act(first)
                second_strategy.act(second)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    tournament([
        (FlameFactory(), NormalStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])

    print("Tournament 1 (error)")
    tournament([
        (TransformCreatureFactory(), AggressiveStrategy()),
        (FlameFactory(), AggressiveStrategy()),
    ])
