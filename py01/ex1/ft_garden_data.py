class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1: Plant = Plant("Rose", 25, 30)
    plant2: Plant = Plant("Sunflower", 80, 45)
    plant3: Plant = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()
