import random


ACHIEVEMENTS = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner",
    "Survivor", "Treasure Hunter", "First Steps",
    "Sharp Mind", "Hidden Path Finder",
    "Dragon Slayer", "Puzzle Master", "Silent Assassin",
    "Iron Will", "Lucky Charm", "Phantom",
    "Beast Tamer", "Archmage", "Sharpshooter"
    ]


def gen_player_achievements() -> set[str]:
    a_count: int = random.randint(8, 12)
    player: set[str] = set(random.sample(ACHIEVEMENTS, a_count))
    return player


def main() -> None:
    c = "\033[32m"
    r = "\033[0m"
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
        print(f"Player {name}: {c}{achievements}{r}")
        print()
    print()
    distinct_achievements: set[str] = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {c}{distinct_achievements}{r}")
    print()
    common_achievements: set[str] = alice.intersection(bob, charlie, dylan)
    print(f"Common to all players: {c}{common_achievements}{r}")
    print()
    a_others: set[str] = bob | charlie | dylan
    alice_only: set[str] = alice.difference(a_others)
    print(f"Only Alice has: {c}{alice_only}{r}")
    print()
    b_others: set[str] = alice | charlie | dylan
    bob_only: set[str] = bob.difference(b_others)
    print(f"Only Bob has: {c}{bob_only}{r}")
    print()
    c_others: set[str] = bob | alice | dylan
    charlie_only: set[str] = charlie.difference(c_others)
    print(f"Only Charlie has: {c}{charlie_only}{r}")
    print()
    d_others: set[str] = bob | charlie | alice
    dylan_only: set[str] = dylan.difference(d_others)
    print(f"Only Dylan has: {c}{dylan_only}{r}")
    print()
    all: set[str] = set(ACHIEVEMENTS)
    print(f"Alice is missing: {c}{all.difference(alice)}{r}")
    print()
    print(f"Bob is missing: {c}{all.difference(bob)}{r}")
    print()
    print(f"Charlie is missing: {c}{all.difference(charlie)}{r}")
    print()
    print(f"Dylan is missing: {c}{all.difference(dylan)}{r}")


if __name__ == "__main__":
    main()
