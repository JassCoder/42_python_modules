class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = float(height)
        self.initial_height: float = float(height)
        self._age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        if self.name == "Rose":
            growth_rate: float = 0.8
        elif self.name == "Sunflower":
            growth_rate = 2.0
        elif self.name == "Cactus":
            growth_rate = 0.2
        else:
            growth_rate = 0.5
        self.height = round(self.height + growth_rate, 2)

    def age(self, days: int = 1) -> None:
        self._age += days

    def weekly_growth(self) -> float:
        return round(self.height - self.initial_height, 2)


if __name__ == "__main__":
    plant: Plant = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    plant.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()

    print(f"Growth this week: {plant.weekly_growth()}cm")
