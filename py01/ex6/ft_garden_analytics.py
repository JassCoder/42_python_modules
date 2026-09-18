class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def log_grow(self) -> None:
            self._grow_count += 1

        def log_age(self) -> None:
            self._age_count += 1

        def log_show(self) -> None:
            self._show_count += 1

        def get_grow_count(self) -> int:
            return self._grow_count

        def get_age_count(self) -> int:
            return self._age_count

        def get_show_count(self) -> int:
            return self._show_count

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )

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

        self._stats: Plant.Stats = self.Stats()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> "Plant.Stats":
        return self._stats

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

    def grow(self, amount: float | None = None) -> None:
        self._stats.log_grow()
        if amount is not None:
            self._height = round(self._height + amount, 2)
        else:
            if self._name == "Rose":
                growth_rate: float = 8.0
            elif self._name == "Sunflower":
                growth_rate = 30.0
            elif self._name == "Cactus":
                growth_rate = 0.2
            elif self._name == "Tomato":
                growth_rate = 2.1
            else:
                growth_rate = 0.5
            self._height = round(self._height + growth_rate, 2)

    def age(self, days: int = 1) -> None:
        self._stats.log_age()
        self._age += days

    def show(self, prefix: str = "") -> None:
        self._stats.log_show()
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
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def log_shade(self) -> None:
            self._shade_count += 1

        def get_shade_count(self) -> int:
            return self._shade_count

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = float(trunk_diameter)
        self._tree_stats: Tree.TreeStats = self.TreeStats()
        self._stats = self._tree_stats

    def get_stats(self) -> "Tree.TreeStats":
        return self._tree_stats

    def produce_shade(self) -> None:
        self._tree_stats.log_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide."
        )

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seed_count: int = 0,
    ) -> None:
        super().__init__(name, height, age, color)
        self._seed_count: int = seed_count
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = self._seed_count

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f"Seeds: {self._seeds}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )

    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("=== Seed")
    sunflower: Seed = Seed("Sunflower", 80.0, 45, "yellow", 42)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("=== Anonymous")
    anon: Plant = Plant.anonymous()
    anon.show()
    display_plant_stats(anon)
