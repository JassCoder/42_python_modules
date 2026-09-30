import random


ACHIEVEMENTS = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner",
    "Survivor", "Treasure Hunter", "First Steps",
    "Sharp Mind", "Hidden Path Finder",
    ]


def gen_player_achievements() -> set[str]:
    a_count: int = random.randint(6, 10)
    player: set[str] = set(random.sample(ACHIEVEMENTS, a_count))
    return player


def main() -> None:
    print("=== Achievement Tracker System ===")
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()
    players: list[tuple[str, set[str]]] = [
        ("Alice", alice), ("Bob", bob),
        ("Charlie", charlie), ("Dylan", dylan)
        ]
    for name, achievements in players:
        print(f"Player {name}: {achievements}")
        print()
    distinct_achievements: set[str] = alice.union(bob, charlie, dylan)
    common_achievements: set[str] = alice.intersection(bob, charlie, dylan)
    print(f"All distinct achievements: {distinct_achievements}")
    print(f"Common to all players: {common_achievements}")
    print(f"Alice only (not Bob): {alice.difference(bob)}")
    print(f"Bob only (not Alice): {bob.difference(alice)}")


if __name__ == "__main__":
    main()
