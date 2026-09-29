import random


ACHIEVEMENTS = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner",
    "Survivor", "Treasure Hunter", "First Steps",
    "Sharp Mind", "Hidden Path Finder",
    ]


def gen_player_achievements() -> set:
    a_count: int = random.randint(6, 10)
    player: set = set(random.sample(ACHIEVEMENTS, a_count ))
    return player


def main() -> None:
    print("=== Achievement Tracker System ===")
    alice: set = gen_player_achievements()
    bob: set = gen_player_achievements()
    charlie: set = gen_player_achievements()
    dylan: set = gen_player_achievements()
    
    
    players: list = [("Alice", alice), ("Bob", bob),
                    ("Charlie", charlie), ("Dylan", dylan)]
    
    for name , achievements in players:
        print(f"Player {name}: {achievements}")
        print()
    print()
    distinct_achievements: set = set().union(alice, bob, charlie, dylan)
    common_achievements: set = set().intersection(alice, bob, charlie, dylan)
    all_achievements: set = set().union(alice, bob, charlie, dylan)
    print(f"All distinct achievements: {distinct_achievements}")


if __name__ == "__main__":
    main()
