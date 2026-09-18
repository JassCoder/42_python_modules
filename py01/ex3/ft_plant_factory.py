class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = float(height)
        self._age: int = age

    def show(self, prefix: str = "") -> None:
        print(
            f"{prefix}{self.name}: {self.height:.1f}cm, "
            f"{self._age} days old"
        )

    def grow(self) -> None:
        if self.name == "Rose":
            growth_rate: float = 0.8
        elif self.name == "Sunflower":
            growth_rate = 2.0
        elif self.name == "Cactus":
            growth_rate = 0.2
        elif self.name == "Oak":
            growth_rate = 0.5
        elif self.name == "Fern":
            growth_rate = 0.4
        else:
            growth_rate = 0.5
        self.height = round(self.height + growth_rate, 2)

    def age(self, days: int = 1) -> None:
        self._age += days


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.show("Created: ")
