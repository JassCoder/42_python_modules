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
    print("=== Achievement Tracker System ===")
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    distinct_achievements: set[str] = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {distinct_achievements}")

    common_achievements: set[str] = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common_achievements}")

    a_others: set[str] = bob | charlie | dylan
    alice_only: set[str] = alice.difference(a_others)
    print(f"Only Alice has: {alice_only}")

    b_others: set[str] = alice | charlie | dylan
    bob_only: set[str] = bob.difference(b_others)
    print(f"Only Bob has: {bob_only}")

    c_others: set[str] = bob | alice | dylan
    charlie_only: set[str] = charlie.difference(c_others)
    print(f"Only Charlie has: {charlie_only}")

    d_others: set[str] = bob | charlie | alice
    dylan_only: set[str] = dylan.difference(d_others)
    print(f"Only Dylan has: {dylan_only}")

    all_achievements: set[str] = set(ACHIEVEMENTS)
    print(f"Alice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
