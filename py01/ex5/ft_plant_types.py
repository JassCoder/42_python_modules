class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height: float = 0.0
        else:
            self._height = float(height)

        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age: int = 0
        else:
            self._age = age

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = float(height)
        val = int(self._height) if self._height.is_integer() else self._height
        print(f"Height updated: {val}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    def grow(self) -> None:
        if self._name == "Rose":
            growth_rate: float = 0.8
        elif self._name == "Sunflower":
            growth_rate = 2.0
        elif self._name == "Cactus":
            growth_rate = 0.2
        elif self._name == "Tomato":
            growth_rate = 2.1
        else:
            growth_rate = 0.5
        self._height = round(self._height + growth_rate, 2)

    def age(self, days: int = 1) -> None:
        self._age += days

    def show(self, prefix: str = "") -> None:
        print(
            f"{prefix}{self._name}: {self._height:.1f}cm, "
            f"{self._age} days old"
        )


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide."
        )

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season: str = harvest_season
        self._nutritional_value: float = 0.0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += 0.5 * days

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {int(self._nutritional_value)}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato: Vegetable = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
