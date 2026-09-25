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
    
    print(f"Player Alice: {alice}")
    print()
    print(f"Player Bob: {bob}")
    print()
    print(f"Player Charlie: {charlie}")
    print()
    print(f"Player Dylan: {dylan}")
    print()



if __name__ == "__main__":
    main()