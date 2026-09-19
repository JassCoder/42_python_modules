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
        if self._height.is_integer():
            val: float = int(self._height)
        else:
            val = self._height
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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant: Plant = Plant("Rose", 15.0, 10)
    plant.show("Plant created: ")
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    plant.set_age(-10)
    print()
    plant.show("Current state: ")
