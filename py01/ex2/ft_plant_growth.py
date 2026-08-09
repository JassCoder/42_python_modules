class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.initial_height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        if (self.name == "Rose"):
            growth_rate = 0.8
        elif (self.name == "Sunflower"):
            growth_rate = 2.0
        elif (self.name == "Cactus"):
            growth_rate = 0.2
        else:
            growth_rate = 0.5
        self.height = round(self.height + growth_rate, 2)
        self.age += 1

    def weekly_growth(self):
        return (round(self.height - self.initial_height, 2))


plant1: Plant = Plant("Rose", 25.0, 30)
plant2: Plant = Plant("Sunflower", 80.0, 45)
plant3: Plant = Plant("Cactus", 15.0, 120)
print("=== Garden Plant Growth ===")
plant1.show()
for day in range(1, 8):
    print(f"=== Day {day} ===")
    plant1.grow()
    plant1.show()

print(f"Growth this week: {plant1.weekly_growth()}cm")
